/*
  transaction.js -- Router for the GPT app
*/
const express = require('express');
const router = express.Router();
const TransactionItem = require('../models/GPTItem')//renamed
const User = require('../models/User');
const GPTItem = require('../models/GPTItem');


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// router.get('/gpt', isLoggedIn, async (req, res) => {
  
//   const items = await GPTItem.find().populate('userId');
//   res.render('gpt', { items, user: req.user });
// });


// // get the value associated to the key
router.get('/gpt',
  isLoggedIn,
  async (req, res, next) => {
    // const show = req.query.show
    // const sortBy = req.query.sortBy
    // const amount = sortBy == 'amount'
      let items=[]
      res.locals.items = await GPTItem.find({userId:req.user._id})
      
      
    //   if (sortBy=="amount") { // show is completed or todo, so just show some items
    //   res.locals.items = await TransactionItem.find({userId:req.user._id}).sort({amount:1}) // removed ,completed
    

    //  } else {
    //  res.locals.items = await TransactionItem.find({userId:req.user._id})


    //  }
            res.render('gpt');//removed ,{items,show} ,completed
});//changed from GPTList



/* add the value in the body to the list associated to the key 
Post would create a new transaction item
resume: String,
  person_desc: Number,
  jobpost: String,
*/
router.post('/gpt',
  isLoggedIn,
  async (req, res, next) => {
      
      
      //get the response
      const axios = require('axios')
      response_gpt =
      await axios.post('http://gracehopper.cs-i.brandeis.edu:3500/openai',
      {prompt:"This is my resume: \n"+ req.body.resume +" This is the job description: "+
        req.body.jobpost+ "Please write a custom cover letter for this job position."})
      // res.json(response_gpt.data)
      // viewing the path /openai_demo will generate the following response:
      // where the answer is in response.data.choices[0].message.content
      // console.log("response_gpt.data", response_gpt.data)
      // console.log("response_gpt.data.choices[0].message.content\n", response_gpt.data.choices[0].message.content)
      req.body.response = response_gpt.data.choices[0].message.content;

      const gpt_item = new GPTItem(
        {resume: req.body.resume,
          // for some reason amount is being stored in category
         person_desc: req.body.person_desc,
         jobpost: req.body.jobpost,
         response: req.body.response,
         remade_resume: req.body.remade_resume,
         userId: req.user._id //this one doesnt need ,stuf . it knows 
        })

      // res.locals.items = req.body.response
      
        // res.locals.database = gpt_item
        
      await gpt_item.save();//save the item

      res.redirect('/gpt')//it'll now go back to same page. 
      // res.render('gpt')
});

router.post('/gpt/get_resp',isLoggedIn,
async (req, res, next) => {
  const request_item = "hi";
});

// router.delete('/gpt/:person_desc', isLoggedIn, async (req, res, next) => {
//   try {
//     const gpt_item = await GPTItem.findOneAndDelete({ person_desc: req.params.person_desc, userId: req.user._id });
//     if (!gpt_item) {
//       return res.status(404).send("Item not found.");
      
//     }
//     res.redirect('/gpt');
//   } catch (err) {
//     next(err);
//   }
// });

//remove
//bf : missed ./
router.post('/gpt/delete', isLoggedIn, async (req, res) => {
  const { person_desc } = req.body.person_desc;
  console.log("Hit /gpt/delete req");
  console.log("req", req);
  // Find the first item in the collection with a matching person_desc value
  const item = await GPTItem.deleteOne({ person_desc });

  if (item) {
    res.send(`Item with person_desc ${person_desc} deleted successfully`);
  } else {
    res.send(`No item found with person_desc ${person_desc}`);
  }
});



router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:itemId")
      await TransactionItem.deleteOne({_id:req.params.itemId});
      res.redirect('/transaction')
});



//we want to find one and prefill the form so the user can edit
router.get('/transaction/transactionEdit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/transactionEdit/:itemId")
      const item = await TransactionItem.findById(req.params.itemId);
      // res.json(item); //sending item as json object but we want to send to edit page
      res.locals.item = item
      res.render('transactionEdit')
      //this is another way to send it
      // res.locals.item = item
      // res.render('edit')

});

router.post('/transaction/updateTransactionItem',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,item,amount,category,date} = req.body;
      //const itemId = req.body.itemID
      //const item = req.body.item
      //const itemId = req.body.priority
      console.log("inside /transaction/:itemId");
      await TransactionItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {item,amount,category,date}});
      res.redirect('/transaction')
});






module.exports = router;
