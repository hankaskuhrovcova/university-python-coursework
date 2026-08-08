#!/usr/bin/env python3

import ast


class BankAccount:
    account_number = 1

    def __init__(self, balance, name):
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1
        self.balance = balance
        self.name = name

    def __str__(self):
        return (
            f"Account number: {self.account_number}\n"
            f"Name: {self.name}\n"
            f"Balance: {self.balance}\n"
        )

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def lodge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class StudentBankAccount(BankAccount):
    def __init__(
        self,
        balance,
        name,
        student_id,
        university
    ):
        super().__init__(balance, name)
        self.student_id = student_id
        self.university = university

    def __str__(self):
        return (
            f"Account number: {self.account_number}\n"
            f"Name: {self.name}\n"
            f"Balance: {self.balance}\n"
            f"Student Id: {self.student_id}\n"
            f"Univeristy: {self.university}\n"
        )
