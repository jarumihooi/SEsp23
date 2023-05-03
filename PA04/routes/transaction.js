/*
  transaction.js -- Router for the Transac app
*/
const express = require('express');
const router = express.Router();
const TransactionItem = require('../models/TransactionItem')//renamed
const User = require('../models/User')


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

// get the value associated to the key
router.get('/transaction',
  isLoggedIn,
  async (req, res, next) => {
    // const show = req.query.show
    const sortBy = req.query.sortBy
    const amount = sortBy == 'amount'

      
      let items=[]
      if (sortBy=="amount") { // show is completed or todo, so just show some items
      res.locals.items = await TransactionItem.find({userId:req.user._id}).sort({amount:1}) // removed ,completed
    

     } else {
     res.locals.items = await TransactionItem.find({userId:req.user._id})


     }
            res.render('transactionList');//removed ,{items,show} ,completed
});//changed from transacitonList



/* add the value in the body to the list associated to the key 
Post would create a new transaction item*/
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const transac = new TransactionItem(
        {description: req.body.description,
          // for some reason amount is being stored in category
         amount: parseInt(req.body.amount),
         category: req.body.category,
         date: req.body.date,
         userId: req.user._id //this one doesnt need ,stuf . it knows 
        })
      await transac.save();//save the item
      res.redirect('/transaction')//it'll now go back to same page. 
});

//remove
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
