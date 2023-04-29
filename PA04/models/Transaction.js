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
  description: String,
  amount: String,
  category: String,
  date: Date,
  userId: {type:ObjectId, ref:'user' }
  //verifies thats a psecific transaction for the user. 
} );
//we can change amount : Number later
module.exports = mongoose.model( 'TransactionItem', transactionSchema );
