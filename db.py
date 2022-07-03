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
                'profile': 0,
                'job': 'unemployed',
                'active_booster': '1'
            }
        )

async def get_wallet(_id):
    await open_profile(_id)
    user = profile.find_one({'_id': _id})
    return user['wallet']

async def get_profile(_id):
    await open_profile(_id)
    user = profile.find_one({'_id': _id})
    return user['profile']

async def update_wallet(_id, amount):
    #if _id == 931973678021873795:
        #return
    await open_profile(_id)
    booster = await get_booster(_id)
    booster = float(booster)
    wallet_amt = await get_wallet(_id)
    profile.update_one({'_id': _id,}, {'$set': {'wallet': wallet_amt+int(amount)}})

async def update_profile(_id, amount):
    await open_profile(_id)
    profile_amt = await get_profile(_id)
    profile.update_one({'_id': _id,}, {'$set': {'profile': profile_amt+int(amount)}})

async def deposit_amt(_id, amount):
    await open_profile(_id)
    await update_wallet(_id, -1*amount)
    await update_profile(_id, amount)

async def withdraw_amt(_id, amount):
    await open_profile(_id)
    await update_profile(_id, -1*amount)
    await update_wallet(_id, amount)

async def get_current_job(_id):
    return profile.find_one({'_id': _id})

# job
# --------------------------------------------------------



# shop
# --------------------------------------------------------
async def buy(item_id, user_id):
    profile.update_one({'_id': user_id}, {'$push': {'items': item_id}})

async def get_inv(user_id):
    user = profile.find_one({'_id': user_id})
    user_inv = user['items']
    return user_inv

async def get_booster(_id):
    user = profile.find_one({'_id': _id})
    return user['active_booster']

async def get_active_items(_id):
    user = profile.find_one({'_id': _id})
    return user['active_items']

async def use_item(_id, item_id):
    profile.update_one({'_id': _id}, {'$pull': {'items': item_id}})
    profile.update_one({'_id': _id}, {'$push': {'active_items': item_id}})

async def use_booster(_id, booster_id):
    booster = await get_booster(booster_id)
    profile.update_one({'_id': _id}, {'$pull': {'items': booster_id}})
    profile.update_one({'_id': _id}, {'$push': {'active_items': booster_id }})
    profile.update_one({'_id': _id}, {'$set': {'active_booster': float(booster)}})