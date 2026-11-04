{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ea8253d2-194a-4f78-8291-156080bd3973",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'set'> <class 'set'> <class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "#sets\n",
    "s={1,2,3,5}\n",
    "s1=set()\n",
    "s2={}\n",
    "print(type(s),type(s1),type(s2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "263589e8-f7e2-46d7-9637-f124bdac0d16",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 5, 10}\n"
     ]
    }
   ],
   "source": [
    "#add(element)\n",
    "s.add(10)\n",
    "print(s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a2cbc26e-2237-4e6d-bfb5-91f5422c2a9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 5}\n"
     ]
    }
   ],
   "source": [
    "#remove\n",
    "s.remove(10)\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5448eaa4-41b3-4067-9186-208c5edce671",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3}\n"
     ]
    }
   ],
   "source": [
    "#discard(element)\n",
    "s.discard(5)\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f21a46ed-d23a-4bc7-a905-6ce93168b73e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{50, 20, 40, 10, 60, 30}\n"
     ]
    }
   ],
   "source": [
    "#set operation\n",
    "s1={10,20,30,40}\n",
    "s2={40,50,60}\n",
    "print(s1.union(s2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "63bee089-c4d5-4bd5-b72d-5020453eeaa8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{40}\n"
     ]
    }
   ],
   "source": [
    "#set intersection operation\n",
    "s1={10,20,30,40}\n",
    "s2={40,50,60}\n",
    "print(s1.intersection(s2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c5a41fe6-6dbd-404f-908c-8b1586dae3fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{10, 20, 30}\n",
      "{10, 20, 30}\n",
      "{50, 60}\n",
      "{50, 60}\n"
     ]
    }
   ],
   "source": [
    "#set difference operation\n",
    "s1={10,20,30,40}\n",
    "s2={40,50,60}\n",
    "print(s1.difference(s2))\n",
    "print(s1-s2)\n",
    "print(s2.difference(s1))\n",
    "print(s2-s1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "796eccc1-c2d2-45c3-8cd6-f15009786412",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{10, 50, 20, 60, 30}\n",
      "{10, 50, 20, 60, 30}\n"
     ]
    }
   ],
   "source": [
    "#set symmetric difference operation\n",
    "s1={10,20,30,40}\n",
    "s2={40,50,60}\n",
    "print(s1.symmetric_difference(s2))\n",
    "print(s1^s2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e5edf68-ae6c-4b75-bd45-8ba75d5ab976",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
