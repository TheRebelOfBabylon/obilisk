from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	equation = db.Column(db.String(5000), index=True, unique=False)
	invoice = db.Column(db.String(257), index=True, unique=True)
	r_hash = db.Column(db.String(56), index=True, unique=True)

	def __repr__(self):
		return '<User {}>'.format(self.invoice)