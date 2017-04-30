from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return '<%r>' % self.name


class Nicotine(models.Model):
    producer_name = models.CharField(max_length=64)
    concentration = models.IntegerField(default=0)

    def __str__(self):
        return '<Nicotine %r>' % self.producer_name


class Flavoring(models.Model):
    name = models.CharField(max_length=64)
    producer = models.CharField(max_length=64)

    def __str__(self):
        return '<Flavor %r Producer %r>' % (self.name, self.producer)


class UsersFlavoringInventory(models.Model):
    user = models.ForeignKey(User)
    flavoring = models.ForeignKey(Flavoring)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return '<User id %r, flavor id %r, amount %r>' % (self.user_id, self.flavor_id, self.amount)


class UsersNicotineInventory(models.Model):
    user_id = models.ForeignKey(User)
    nicotine_id = models.ForeignKey(Nicotine)
    amount = models.IntegerField(default=0)


class ELiquid(models.Model):
    name = models.CharField(max_length=64)
    flavoring = models.ManyToManyField(Flavoring, through='Composition')

    def __str__(self):
        return '<eLiquid %r>' % self.name


class Composition(models.Model):
    eLiquid = models.ForeignKey(ELiquid, on_delete=models.CASCADE)
    flavorings = models.ForeignKey(Flavoring, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '<eLiquid %r flavorings %r quantity %r>' % (self.eLiquid, self.flavorings, self.quantity)


class UsersFavouriteELiquids(models.Model):
    user_id = models.ForeignKey(User)
    eliquid_id = models.ForeignKey(ELiquid)


# Users_Flavor_Inventories = db.Table('Users_Flavor_Inventories',
#                                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#                                     db.Column('flavor_id', db.Integer, db.ForeignKey('flavor.id')),
#                                     db.Column('amount', db.SmallInteger)
#                                     )

# eLiquids_Compositions = db.Table('eLiquids_compositions',
#                                  db.Column('eliquid_id', db.Integer, db.ForeignKey('eLiquids.id')),
#                                  db.Column('flavor_id', db.Integer, db.ForeignKey('Flavors.id')),
#                                  db.Column('quantity', db.SmallInteger)
#                                  )
#

#
# Users_Nicotine_Inventories = db.Table('User_Nicotine_Inventories',
#                                       db.Column('user_id', db.Integer, db.ForeignKey('Users.id')),
#                                       db.Column('nicotine_id', db.Integer, db.ForeignKey('Nicotine.id')),
#                                       db.Column('amount', db.SmallInteger)
#                                       )
#
# Users_Favourite_ELiquids = db.Table('Users_Favourite_eLiquids',
#                                     db.Column('user_id', db.Integer, db.ForeignKey('Users.id')),
#                                     db.Column('eliquid_id', db.Integer, db.ForeignKey('eLiquids.id')),
#                                     )

