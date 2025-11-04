from database import db
from models.punk_model import punk_model

class PunkRepository:

    def get_all():
        return punk_model.query.all()
    
    def get_by_id(self,token_id):
        punkM=punk_model.query.get(token_id)
        if punkM:
            return punkM
        return None
    
    def create(token_id,owner,priceETH,imageURL,listed,traits,top_offerETH,last_saleETH):
        punkM=punk_model(token_id,owner,priceETH,imageURL,listed,traits,top_offerETH,last_saleETH)
        db.session.add(punkM)
        db.session.commit()
    
    def update(self, token_id,up_data):
        punkM=punk_model.query.get(token_id)
        if not punkM:
            return None
        for k,v in up_data.items():
            setattr(punkM,k,v)
            db.session.commit()
        return punkM

    def delete(self,token_id):
        punkM=self.get_by_id(token_id)
        if punkM:
          db.session.delete(punkM)
          db.session.commit()
        return punkM
