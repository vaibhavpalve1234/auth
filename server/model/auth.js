const mongoose = require('mongoose')
// import {nanoid} from 'nanoid';

const { Schema } = mongoose

const userSchema = new Schema(
    {
        name: {
            type: String,
            trim: true,
            required: true
        },
        email: {
            type: String,
            trim: true,
            required: true,
            unique: true
        },
        password: {
            type: String,
            required: true,
            unique: true,
        },
        address: {
            type: String,
            trim: true,
        },
        role: {
            type: Number,
            default: 0,
        }
    },
    {
        timestamps: true
    }
)
module.exports = mongoose.model("User", userSchema)