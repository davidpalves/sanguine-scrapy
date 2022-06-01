from api.app import mongo, scheduler
from api.common.helpers import force_data_update, notify_user_able_to_donate
from api.models.users import User

@scheduler.task("cron", id="update_data", hour=9, minute=15)
def trigger_update():
    from api.app import app
    with app.app_context():
        force_data_update()

@scheduler.task("cron", id="update_data", hour=10, minute=30)
def notify_users_for_banks_in_need():
    from api.app import app
    with app.app_context():
        bancos_sangue = mongo.db.niveis
        
        cities_in_need = []
        
        for banco in bancos_sangue.find():
            niveis = banco["sangue"].values()
            if "alerta" in niveis or "critica" in niveis:
                cities_in_need.append(banco["cidade"])
            else:
                continue

        users_to_be_notified = User.query.filter(User.cidade.in_(cities_in_need)).all()

        for user in users_to_be_notified:
            if user.is_able_to_donate:
                notify_user_able_to_donate(user=user)
            continue