/*To start we would need mongoose
Create schema 
create objid
exportmodel
*/


'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;//id for the object

//defining something with mongoose, in js.
var transactionSchema = Schema( {
  resume: String,
  person_desc: Number,
  jobpost: String,
  response: String,
  remade_resume: String,
  //date: String,
  userId: {type:ObjectId, ref:'user' },

  //verifies thats a specific transaction for the user. 
} );
module.exports = mongoose.model( 'GPTItem', transactionSchema );


/*
resume: String,
  person_desc: Number,
  jobpost: String,*/