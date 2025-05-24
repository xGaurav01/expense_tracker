from flask import Blueprint, request, jsonify
from services.expense_service import add_expense, get_expenses_by_user, update_expense, delete_expense
from middleware.auth import login_required

expense_bp = Blueprint('expense', __name__)

@expense_bp.route('/expenses', methods=['POST'])
@login_required
def api_add_expense():
    data = request.get_json()
    expense_id = add_expense(
        request.user_id,
        data['amount'],
        data['category'],
        data['description'],
        data['date']
    )
    return jsonify({"message": "Expense added Successfully", "Expense Id": expense_id,"Amount":data['amount'],"Category":data['category'],"Description":data['description'],"Date":data['date']}), 201

@expense_bp.route('/expenses', methods=['GET'])
@login_required
def api_get_expenses():
    expenses = get_expenses_by_user(request.user_id)
    return jsonify({"expenses": expenses})

@expense_bp.route('/expenses/<int:expense_id>', methods=['PUT'])
@login_required
def api_update_expense(expense_id):
    data = request.get_json()
    updated = update_expense(
        expense_id,
        request.user_id,
        data['amount'],
        data['category'],
        data['description'],
        data['date']
    )
    if updated:
        return jsonify({"message": "Expense updated Successfully"}),200
    return jsonify({"error": f"Expense with id {expense_id } not found"}), 404

@expense_bp.route('/expenses/<int:expense_id>', methods=['DELETE'])
@login_required
def api_delete_expense(expense_id):
    deleted = delete_expense(expense_id,request.user_id)
    if deleted:
        return jsonify({"message": "Expense deleted"})
    return jsonify({"error": "Expense not found"}), 404
