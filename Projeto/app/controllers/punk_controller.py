from flask import Blueprint,jsonify,request
from repositories.punk_repository import PunkRepository
from services.punk_service import PunkService

punkbp=Blueprint('punks',__name__)
punkRepo=PunkRepository()
punkServ=PunkService(punkRepo)

@punkbp.route('/item/<int: token_id>',methods=['GET'])
def get_punk_id(token_id):
    return jsonify(punkServ.get_by_id(token_id))

@punkbp.route('/collection',methods=['GET'])
def all_punks():
    return jsonify(punkServ.get_all_punk())

@punkbp('/create',methods=['POST'])
def create_punk():
    data=request.get_json() or {}
    try:
        punk=punkServ.create_punk(data)
    except ValueError as e:
        return jsonify({'Erro':str(e)}),400
    
@punkbp.route('/update/<int: token_id>',methods=['PUT'])
def update_punk(token_id):
        data=request.get_json() or {}
        punk=punkServ.update_punk(token_id,data)
        if not punk:
             return jsonify({'erro':'Not found'}),404
        return jsonify(punk.to_dict())
@punkbp.route('/delete/<int:token_id>',methods=['DELETE'])
def delete_punk(token_id):
     aprov=punkServ.delete_punk(token_id)
     if not aprov:
          return jsonify({'erro':'Not found'}),404
     return jsonify({'deleted':True})