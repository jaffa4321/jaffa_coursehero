from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def add_points(repy_id, gen_points, gen_days,collection):
    user_id = repy_id
    u = int(gen_days)*1
    date = datetime.now()
    date3 = date + relativedelta(days=u+1)
    user = collection.find_one({"user_id": str(user_id)})
    # print(user)
    if user is None:
        collection.insert_one(
            {"user_id": str(user_id), "points": str(gen_points), "timeout": str(date3)})
        return [gen_points, gen_days]
    else:
        old_points = int(user["points"])
        new_points = old_points + int(gen_points)
        old_timeout = user["timeout"]
        time_formate = datetime.strptime(old_timeout, "%Y-%m-%d %H:%M:%S.%f")
        new_time = time_formate + relativedelta(days=int(gen_days))
        update_dict = {"$set": {"points": str(
            new_points), "timeout": str(new_time)}}
        collection.update_one(user, update_dict,  upsert=True)
        new_days = (time_formate - datetime.now()).days
        return [new_points, new_days]

def update_points(reply_id,points,collection):
    user_id = reply_id
    user = collection.find_one({"user_id": str(user_id)})
    if user is None:
        return False
    else:
        update_dict = {"$set": {"points": str(points)}}
        collection.update_one(user, update_dict,  upsert=True)
        return True

def update_days(reply_id,days,collection):
    user_id = reply_id
    user = collection.find_one({"user_id": str(user_id)})
    if user is None:
        return False
    else:
        old_timeout = user["timeout"]
        time_formate = datetime.strptime(old_timeout, "%Y-%m-%d %H:%M:%S.%f")
        new_time = time_formate + relativedelta(days=int(days))
        update_dict = {"$set": {"timeout": str(new_time)}}
        collection.update_one(user, update_dict,  upsert=True)
        return True

def get_data(user_id,collection):
    try:
        user = collection.find_one({"user_id": str(user_id)})
        if user is None:
            return [0,0]
        else:
            old_points = int(user["points"])
            old_timeout = user["timeout"]
            time_formate = datetime.strptime(
                old_timeout, "%Y-%m-%d %H:%M:%S.%f")
            new_days = (time_formate - datetime.now()).days
            n = new_days + 1
            if n <= 0:
                collection.delete_one(user)
                return [0, 0]
            elif old_points <= 0:
                collection.delete_one(user)
                return [0, 0]
            else:
                return [old_points, n]
    except:
        return False
    
def sub_points(user_id,collection):
    try:
        user = collection.find_one({"user_id": str(user_id)})
        old_points = int(user["points"])
        new_points = old_points - 1
        collection.update_one({"user_id": str(user_id)}, {
                              "$set": {"points": str(new_points)}})
        return new_points

    except Exception as e:
        print(e)
        return False
    
def add_cookie(cookie,email,unlockes_remaining,collection):
    coo = collection.find_one({
        "email": email
    })
    if coo is None:
        collection.insert_one({
            "email": email,
            "cookie": cookie,
            "unlockes_remaining":int(unlockes_remaining),
            "status": True
        })
        return True
    else:
        collection.update_one({
            "email": email
        }, {
            "$set": {
                "cookie": cookie,
                "unlockes_remaining":int(unlockes_remaining),
                "status": True
            }
        })
        return True

def get_cookie(collection):
    cookies = collection.find_one({
        "unlockes_remaining": {"$gt": 0},
        "status": {"$eq": True}
    })
    if cookies is None:
        return None
    else:
        return cookies

def update_unlockes_remaining(email,unlockes_remaining,collection):
    try:
        collection.update_one({
            "email": email
        }, {
            "$set": {
                "unlockes_remaining": int(unlockes_remaining)
            }
        })
        return True
    except:
        return False

def update_status(email,collection):
    try:
        collection.update_one({
            "email": email
        }, {
            "$set": {
                "status": False
            }
        })
        return True
    except:
        return False

def cookies_statues(collecion):
    try:
        cookies = collecion.find()
        if cookies is None:
            return None
        return cookies
    except:
        return False