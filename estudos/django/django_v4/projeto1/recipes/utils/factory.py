from random import randint

import faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = faker.Faker('pt_BR')


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2),
        'preparation_time_unit': 'Minute',
        'serving': fake.random_number(digits=2),
        'serving_unit': 'Porção',
        'preparation_steps': fake.text(8000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name()
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio()
        }

    }
