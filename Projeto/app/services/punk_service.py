from repositories.punk_repository import PunkRepository
class PunkService:
    def __int__(self,PunkRepository):
        self.punkRepository=PunkRepository

    def get_all_punk(self):
        return self.punkRepository.get_all()

    def get_by_id(self,token_id):
        return self.punkRepository.get_by_id(token_id)
    
    def create_punk(self,data):
        if 'token_id' not in data:
            raise ValueError('Sem token id')
        return self.punkRepository.create(data)
    
    def update_punk(self,token_id,data):
        return self.punkRepository.update(token_id,data)
    
    def delete_punk(self,token_id):
        return self.punkRepository.delete(token_id)
    