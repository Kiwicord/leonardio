import pymongo
from pymongo import MongoClient
import asyncio

#connection:
cluster = MongoClient('mongodb+srv://lauchrenss:SussyBaka69@cluster0.kfgs1ir.mongodb.net/?retryWrites=true&w=majority', connect=False)
db = cluster['leeenard']

#config:
profile = db['profile']

#main:

async def open_profile(_id):
    if profile.find_one({'_id': _id}):
        return
    else:
        profile.insert_one(
            {
                '_id': _id,
                'wallet': 0,
                'bank': 0,
                'job': 'unemployed',
                'active_booster': '1'
            }
        )

async def get_wallet(_id):
    await open_profile(_id)
    user = profile.find_one({'_id': _id})
    return user['wallet']

async def get_bank(_id):
    await open_profile(_id)
    user = profile.find_one({'_id': _id})
    return user['bank']