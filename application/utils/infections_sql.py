from application import app, db

# whole page
result = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1;")
number_result = result.first()[0]
# dolnoslaskie
result1 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='ds';")
number_result1 = result1.first()[0]
# kujawsko-pomorskie
result2 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='kp';")
number_result2 = result2.first()[0]
# lubelskie
result3 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='lb';")
number_result3 = result3.first()[0]
# lubuskie
result4 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='ls';")
number_result4 = result4.first()[0]
# lodzkie
result5 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='ld';")
number_result5 = result5.first()[0]
# malopolskie
result6 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='mp';")
number_result6 = result6.first()[0]
# mazowieckie
result7 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='mz';")
number_result7 = result7.first()[0]
# opolskie
result8 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='op';")
number_result8 = result8.first()[0]
# podkarpacie
result9 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='pk';")
number_result9 = result9.first()[0]
# podlaskie
result10 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='pl';")
number_result10 = result10.first()[0]
# pomorskie
result11 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='pm';")
number_result11 = result11.first()[0]
# slaskie
result12 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='sl';")
number_result12 = result12.first()[0]
# swietokrzyskie
result13 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='sk';")
number_result13 = result13.first()[0]
# warminsko-mazurskie
result14 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='wm';")
number_result14 = result14.first()[0]
# wielkopolskie
result15 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='wp';")
number_result15 = result15.first()[0]
# zachodnio-pomorskie
result16 = db.engine.execute("SELECT COUNT(*) FROM userinfo WHERE is_infected=1 AND voivodeship='zp';")
number_result16 = result16.first()[0]
