from database import db

class PunkModel(db.Model):
    __tablename__='Cryptopunks'
    id=db.Column(db.Integer,primary_key=True)
    token_id=db.Column(db.Integer,unique=True,nullable=False)
    owner=db.Column(db.String(50),nullable=False)
    priceETH=db.Column(db.Integer,nullable=False)
    last_saleETH=db.Column(db.Float,nullable=True)
    imageURL=db.Column(db.String(100),nullable=False)
    top_offerETH=db.Column(db.Float)
    listed=db.Column(db.Boolean,nullable=False)
    traits=db.Column(JSON,default=[])

    def to_dict(self):
        return {
            'id':self.id,
            'token_id':self.token_id,
            'owner':self.owner,
            'priceETH':self.priceETH,
            'last_saleETH':self.last_saleETH,
            'imageURL':self.imageURL,
            'top_offer':self.top_offerETH,
            'listed':self.listed,
            'traits':self.traits

        }