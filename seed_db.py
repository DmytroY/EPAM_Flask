''' Seed some data to database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from micropeutist.models.model import Doctor, Patient

engine = create_engine('mysql://root:@localhost/micropeutist', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# === Doctors instanses ====
john = Doctor(**{'first_name': 'Jonh',
    'last_name': 'Watson',
    'grade': 'BM',
    'specialization': 'Comban medic',
    'email': 'jh_watson@micropeutist.com'
    })
session.add(john)

stephen = Doctor(**{'first_name': 'Stephen',
    'last_name': 'Strange',
    'grade': 'MS',
    'specialization': 'Neirosurgeon',
    'email': 'its_strange@micropeutist.com'
    })
session.add(stephen)

greg = Doctor(**{'first_name': 'Gregory',
    'last_name': 'House',
    'grade': 'MD',
    'specialization': 'Nephrologist',
    'email': 'house_md@micropeutist.com'
    })
session.add(greg)

victor = Doctor(**{'first_name': 'Victor',
    'last_name': 'Frankenstein',
    'grade': '',
    'specialization': 'Patalogist',
    'email': 'frankenstein@victor.com'
    })
session.add(victor)

# === Patients instances ====
creature = Patient(**{
    'first_name': 'Creature',
    'last_name': 'Victorson',
    'gender': 'male',
    'birthday': '1818-01-01',
    'health_state': 'either alive or dead',
    'email': 'creature@death.io'})
creature.doctor = victor
session.add(creature)

steve = Patient(**{
    'first_name': 'Steve',
    'last_name': 'McQueen',
    'gender': 'male',
    'birthday': '2006-05-03',
    'health_state': 'under diagnosis process',
    'email': 'rat@steve.mc'})
steve.doctor =greg
session.add(steve)

sherlock = Patient(**{
    'first_name': 'Sherlock',
    'last_name': 'Holmes',
    'gender': 'male',
    'birthday': '1854-01-06',
    'health_state': 'Morphine addiction',
    'email': 'sherlock@holmes.det'})
sherlock.doctor = john
session.add(sherlock)

laura = Patient(**{
    'first_name': 'Laura',
    'last_name': 'Capway',
    'gender': 'female',
    'birthday': '2005-11-16',
    'health_state': 'healthy',
    'email': 'laura@email.com'})
laura.doctor = john
session.add(laura)

# commit
session.commit()
session.close()

