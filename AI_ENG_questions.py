{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# 9/24 Q1: class attributes, instance method and class method\n",
        "Create a Employee class, with raise_amount = 1.05 as class attribute, with name and salary as instance attribute, and a instance method that apply raise to each employee’s salary, a class method that set raise_amount for the employee class, with a static method checking whether today is workday.\n",
        "\n",
        "calculate the raised salary of John, with base salary of 50000,\n",
        "\n",
        "calculate the raised salary of Jane, with base salary of 60000,\n",
        "\n",
        "change raise_amount = 1.1\n",
        "\n",
        "recalculate the raised salary of Jane and John\n",
        "\n",
        "check if today is workday"
      ],
      "metadata": {
        "id": "11dsv8cVWf-8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import datetime\n",
        "\n",
        "class Employee:\n",
        "  raise_amount = 1.05\n",
        "\n",
        "  def __init__(self,name,salary):\n",
        "    self.name = name\n",
        "    self.salary = salary\n",
        "\n",
        "  def raise_salary(self):\n",
        "    self.salary = self.salary * self.raise_amount\n",
        "\n",
        "  def set_raise_amount(amount):\n",
        "    Employee.raise_amount = amount\n",
        "\n",
        "  def check_workday():\n",
        "    return datetime.today().weekday() <6\n",
        ""
      ],
      "metadata": {
        "id": "sr2MbSYnexKv"
      },
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 50,
      "metadata": {
        "id": "oD1AY14xDUT5"
      },
      "outputs": [],
      "source": [
        "employee1 = Employee('John',50000)\n",
        "employee2 = Employee('Jane',60000)\n",
        "\n",
        "employee1.raise_salary()\n",
        "employee2.raise_salary()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Employee {}' salary: {}\".format(employee1.name,employee1.salary))\n",
        "print(\"Employee {}' salary: {}\".format(employee2.name,employee2.salary))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Stqmc_0NlJjn",
        "outputId": "44cabaf9-4378-4c45-e3da-0f558fc2b2cf"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Employee John' salary: 52500.0\n",
            "Employee Jane' salary: 63000.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Employee.set_raise_amount(amount=1.1)\n",
        "print(\"current_raise_amount:{}\".format(Employee.raise_amount))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4NhE7-FylOl9",
        "outputId": "cf90cb5a-1d2d-4397-f78f-462d9f63ce21"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "current_raise_amount:1.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Is today a workday?{}\".format(Employee.check_workday()))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qpiPQ-KEmD2l",
        "outputId": "a36ff9bd-81ef-474c-8d99-554fd280d0af"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Is today a workday?True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "eGWaOgwym4P6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CAvh_ri5p7v3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}