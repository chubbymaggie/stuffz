#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    alu32bits.py - ALU 32bits with full 1bit adder in Python --
#    Useful when you want to obfuscate 32 bits integer additions :))) (o\ @__x86)
#    Copyright (C) 2013 Axel "0vercl0k" Souchet - http://www.twitter.com/0vercl0k
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys

def full_adder32(A, B):
    """
    ALU 1bit:
    A B Cin | Cout S
    ----------------
    0 0 0   | 0    0
    0 0 1   | 0    1
    0 1 0   | 0    1
    0 1 1   | 1    0
    1 0 0   | 0    1
    1 0 1   | 1    0
    1 1 0   | 1    0
    1 1 1   | 1    1

    S = Or(
        And(Not(A), B, Not(Cin)),
        And(A, Not(B), Not(Cin)),
        And(Not(A), Not(B), Cin),
        And(A, B, Cin)
    )

    Cout = Or(
        And(Not(A), B, Cin),
        And(A, Not(B), Cin),
        And(A, B, Not(Cin)),
        And(A, B, Cin)
    )
    """
    R0 = ((~((A >> 0) & 1)) & ((B >> 0) & 1) & (1)) | (((A >> 0) & 1) & (~((B >> 0) & 1)) & (1)) | ((~((A >> 0) & 1)) & (~((B >> 0) & 1)) & (0)) | (((A >> 0) & 1) & ((B >> 0) & 1) & (0))
    Cout0 = ((~((A >> 0) & 1)) & ((B >> 0) & 1) & (0)) | (((A >> 0) & 1) & (~((B >> 0) & 1)) & (0)) | (((A >> 0) & 1) & ((B >> 0) & 1) & (1)) | (((A >> 0) & 1) & ((B >> 0) & 1) & (0))
    R1 = ((~((A >> 1) & 1)) & ((B >> 1) & 1) & ~((Cout0))) | (((A >> 1) & 1) & (~((B >> 1) & 1)) & ~((Cout0))) | ((~((A >> 1) & 1)) & (~((B >> 1) & 1)) & (Cout0)) | (((A >> 1) & 1) & ((B >> 1) & 1) & (Cout0))
    Cout1 = ((~((A >> 1) & 1)) & ((B >> 1) & 1) & (Cout0)) | (((A >> 1) & 1) & (~((B >> 1) & 1)) & (Cout0)) | (((A >> 1) & 1) & ((B >> 1) & 1) & ~((Cout0))) | (((A >> 1) & 1) & ((B >> 1) & 1) & (Cout0))
    R2 = ((~((A >> 2) & 1)) & ((B >> 2) & 1) & ~((Cout1))) | (((A >> 2) & 1) & (~((B >> 2) & 1)) & ~((Cout1))) | ((~((A >> 2) & 1)) & (~((B >> 2) & 1)) & (Cout1)) | (((A >> 2) & 1) & ((B >> 2) & 1) & (Cout1))
    Cout2 = ((~((A >> 2) & 1)) & ((B >> 2) & 1) & (Cout1)) | (((A >> 2) & 1) & (~((B >> 2) & 1)) & (Cout1)) | (((A >> 2) & 1) & ((B >> 2) & 1) & ~((Cout1))) | (((A >> 2) & 1) & ((B >> 2) & 1) & (Cout1))
    R3 = ((~((A >> 3) & 1)) & ((B >> 3) & 1) & ~((Cout2))) | (((A >> 3) & 1) & (~((B >> 3) & 1)) & ~((Cout2))) | ((~((A >> 3) & 1)) & (~((B >> 3) & 1)) & (Cout2)) | (((A >> 3) & 1) & ((B >> 3) & 1) & (Cout2))
    Cout3 = ((~((A >> 3) & 1)) & ((B >> 3) & 1) & (Cout2)) | (((A >> 3) & 1) & (~((B >> 3) & 1)) & (Cout2)) | (((A >> 3) & 1) & ((B >> 3) & 1) & ~((Cout2))) | (((A >> 3) & 1) & ((B >> 3) & 1) & (Cout2))
    R4 = ((~((A >> 4) & 1)) & ((B >> 4) & 1) & ~((Cout3))) | (((A >> 4) & 1) & (~((B >> 4) & 1)) & ~((Cout3))) | ((~((A >> 4) & 1)) & (~((B >> 4) & 1)) & (Cout3)) | (((A >> 4) & 1) & ((B >> 4) & 1) & (Cout3))
    Cout4 = ((~((A >> 4) & 1)) & ((B >> 4) & 1) & (Cout3)) | (((A >> 4) & 1) & (~((B >> 4) & 1)) & (Cout3)) | (((A >> 4) & 1) & ((B >> 4) & 1) & ~((Cout3))) | (((A >> 4) & 1) & ((B >> 4) & 1) & (Cout3))
    R5 = ((~((A >> 5) & 1)) & ((B >> 5) & 1) & ~((Cout4))) | (((A >> 5) & 1) & (~((B >> 5) & 1)) & ~((Cout4))) | ((~((A >> 5) & 1)) & (~((B >> 5) & 1)) & (Cout4)) | (((A >> 5) & 1) & ((B >> 5) & 1) & (Cout4))
    Cout5 = ((~((A >> 5) & 1)) & ((B >> 5) & 1) & (Cout4)) | (((A >> 5) & 1) & (~((B >> 5) & 1)) & (Cout4)) | (((A >> 5) & 1) & ((B >> 5) & 1) & ~((Cout4))) | (((A >> 5) & 1) & ((B >> 5) & 1) & (Cout4))
    R6 = ((~((A >> 6) & 1)) & ((B >> 6) & 1) & ~((Cout5))) | (((A >> 6) & 1) & (~((B >> 6) & 1)) & ~((Cout5))) | ((~((A >> 6) & 1)) & (~((B >> 6) & 1)) & (Cout5)) | (((A >> 6) & 1) & ((B >> 6) & 1) & (Cout5))
    Cout6 = ((~((A >> 6) & 1)) & ((B >> 6) & 1) & (Cout5)) | (((A >> 6) & 1) & (~((B >> 6) & 1)) & (Cout5)) | (((A >> 6) & 1) & ((B >> 6) & 1) & ~((Cout5))) | (((A >> 6) & 1) & ((B >> 6) & 1) & (Cout5))
    R7 = ((~((A >> 7) & 1)) & ((B >> 7) & 1) & ~((Cout6))) | (((A >> 7) & 1) & (~((B >> 7) & 1)) & ~((Cout6))) | ((~((A >> 7) & 1)) & (~((B >> 7) & 1)) & (Cout6)) | (((A >> 7) & 1) & ((B >> 7) & 1) & (Cout6))
    Cout7 = ((~((A >> 7) & 1)) & ((B >> 7) & 1) & (Cout6)) | (((A >> 7) & 1) & (~((B >> 7) & 1)) & (Cout6)) | (((A >> 7) & 1) & ((B >> 7) & 1) & ~((Cout6))) | (((A >> 7) & 1) & ((B >> 7) & 1) & (Cout6))
    R8 = ((~((A >> 8) & 1)) & ((B >> 8) & 1) & ~((Cout7))) | (((A >> 8) & 1) & (~((B >> 8) & 1)) & ~((Cout7))) | ((~((A >> 8) & 1)) & (~((B >> 8) & 1)) & (Cout7)) | (((A >> 8) & 1) & ((B >> 8) & 1) & (Cout7))
    Cout8 = ((~((A >> 8) & 1)) & ((B >> 8) & 1) & (Cout7)) | (((A >> 8) & 1) & (~((B >> 8) & 1)) & (Cout7)) | (((A >> 8) & 1) & ((B >> 8) & 1) & ~((Cout7))) | (((A >> 8) & 1) & ((B >> 8) & 1) & (Cout7))
    R9 = ((~((A >> 9) & 1)) & ((B >> 9) & 1) & ~((Cout8))) | (((A >> 9) & 1) & (~((B >> 9) & 1)) & ~((Cout8))) | ((~((A >> 9) & 1)) & (~((B >> 9) & 1)) & (Cout8)) | (((A >> 9) & 1) & ((B >> 9) & 1) & (Cout8))
    Cout9 = ((~((A >> 9) & 1)) & ((B >> 9) & 1) & (Cout8)) | (((A >> 9) & 1) & (~((B >> 9) & 1)) & (Cout8)) | (((A >> 9) & 1) & ((B >> 9) & 1) & ~((Cout8))) | (((A >> 9) & 1) & ((B >> 9) & 1) & (Cout8))
    R10 = ((~((A >> 10) & 1)) & ((B >> 10) & 1) & ~((Cout9))) | (((A >> 10) & 1) & (~((B >> 10) & 1)) & ~((Cout9))) | ((~((A >> 10) & 1)) & (~((B >> 10) & 1)) & (Cout9)) | (((A >> 10) & 1) & ((B >> 10) & 1) & (Cout9))
    Cout10 = ((~((A >> 10) & 1)) & ((B >> 10) & 1) & (Cout9)) | (((A >> 10) & 1) & (~((B >> 10) & 1)) & (Cout9)) | (((A >> 10) & 1) & ((B >> 10) & 1) & ~((Cout9))) | (((A >> 10) & 1) & ((B >> 10) & 1) & (Cout9))
    R11 = ((~((A >> 11) & 1)) & ((B >> 11) & 1) & ~((Cout10))) | (((A >> 11) & 1) & (~((B >> 11) & 1)) & ~((Cout10))) | ((~((A >> 11) & 1)) & (~((B >> 11) & 1)) & (Cout10)) | (((A >> 11) & 1) & ((B >> 11) & 1) & (Cout10))
    Cout11 = ((~((A >> 11) & 1)) & ((B >> 11) & 1) & (Cout10)) | (((A >> 11) & 1) & (~((B >> 11) & 1)) & (Cout10)) | (((A >> 11) & 1) & ((B >> 11) & 1) & ~((Cout10))) | (((A >> 11) & 1) & ((B >> 11) & 1) & (Cout10))
    R12 = ((~((A >> 12) & 1)) & ((B >> 12) & 1) & ~((Cout11))) | (((A >> 12) & 1) & (~((B >> 12) & 1)) & ~((Cout11))) | ((~((A >> 12) & 1)) & (~((B >> 12) & 1)) & (Cout11)) | (((A >> 12) & 1) & ((B >> 12) & 1) & (Cout11))
    Cout12 = ((~((A >> 12) & 1)) & ((B >> 12) & 1) & (Cout11)) | (((A >> 12) & 1) & (~((B >> 12) & 1)) & (Cout11)) | (((A >> 12) & 1) & ((B >> 12) & 1) & ~((Cout11))) | (((A >> 12) & 1) & ((B >> 12) & 1) & (Cout11))
    R13 = ((~((A >> 13) & 1)) & ((B >> 13) & 1) & ~((Cout12))) | (((A >> 13) & 1) & (~((B >> 13) & 1)) & ~((Cout12))) | ((~((A >> 13) & 1)) & (~((B >> 13) & 1)) & (Cout12)) | (((A >> 13) & 1) & ((B >> 13) & 1) & (Cout12))
    Cout13 = ((~((A >> 13) & 1)) & ((B >> 13) & 1) & (Cout12)) | (((A >> 13) & 1) & (~((B >> 13) & 1)) & (Cout12)) | (((A >> 13) & 1) & ((B >> 13) & 1) & ~((Cout12))) | (((A >> 13) & 1) & ((B >> 13) & 1) & (Cout12))
    R14 = ((~((A >> 14) & 1)) & ((B >> 14) & 1) & ~((Cout13))) | (((A >> 14) & 1) & (~((B >> 14) & 1)) & ~((Cout13))) | ((~((A >> 14) & 1)) & (~((B >> 14) & 1)) & (Cout13)) | (((A >> 14) & 1) & ((B >> 14) & 1) & (Cout13))
    Cout14 = ((~((A >> 14) & 1)) & ((B >> 14) & 1) & (Cout13)) | (((A >> 14) & 1) & (~((B >> 14) & 1)) & (Cout13)) | (((A >> 14) & 1) & ((B >> 14) & 1) & ~((Cout13))) | (((A >> 14) & 1) & ((B >> 14) & 1) & (Cout13))
    R15 = ((~((A >> 15) & 1)) & ((B >> 15) & 1) & ~((Cout14))) | (((A >> 15) & 1) & (~((B >> 15) & 1)) & ~((Cout14))) | ((~((A >> 15) & 1)) & (~((B >> 15) & 1)) & (Cout14)) | (((A >> 15) & 1) & ((B >> 15) & 1) & (Cout14))
    Cout15 = ((~((A >> 15) & 1)) & ((B >> 15) & 1) & (Cout14)) | (((A >> 15) & 1) & (~((B >> 15) & 1)) & (Cout14)) | (((A >> 15) & 1) & ((B >> 15) & 1) & ~((Cout14))) | (((A >> 15) & 1) & ((B >> 15) & 1) & (Cout14))
    R16 = ((~((A >> 16) & 1)) & ((B >> 16) & 1) & ~((Cout15))) | (((A >> 16) & 1) & (~((B >> 16) & 1)) & ~((Cout15))) | ((~((A >> 16) & 1)) & (~((B >> 16) & 1)) & (Cout15)) | (((A >> 16) & 1) & ((B >> 16) & 1) & (Cout15))
    Cout16 = ((~((A >> 16) & 1)) & ((B >> 16) & 1) & (Cout15)) | (((A >> 16) & 1) & (~((B >> 16) & 1)) & (Cout15)) | (((A >> 16) & 1) & ((B >> 16) & 1) & ~((Cout15))) | (((A >> 16) & 1) & ((B >> 16) & 1) & (Cout15))
    R17 = ((~((A >> 17) & 1)) & ((B >> 17) & 1) & ~((Cout16))) | (((A >> 17) & 1) & (~((B >> 17) & 1)) & ~((Cout16))) | ((~((A >> 17) & 1)) & (~((B >> 17) & 1)) & (Cout16)) | (((A >> 17) & 1) & ((B >> 17) & 1) & (Cout16))
    Cout17 = ((~((A >> 17) & 1)) & ((B >> 17) & 1) & (Cout16)) | (((A >> 17) & 1) & (~((B >> 17) & 1)) & (Cout16)) | (((A >> 17) & 1) & ((B >> 17) & 1) & ~((Cout16))) | (((A >> 17) & 1) & ((B >> 17) & 1) & (Cout16))
    R18 = ((~((A >> 18) & 1)) & ((B >> 18) & 1) & ~((Cout17))) | (((A >> 18) & 1) & (~((B >> 18) & 1)) & ~((Cout17))) | ((~((A >> 18) & 1)) & (~((B >> 18) & 1)) & (Cout17)) | (((A >> 18) & 1) & ((B >> 18) & 1) & (Cout17))
    Cout18 = ((~((A >> 18) & 1)) & ((B >> 18) & 1) & (Cout17)) | (((A >> 18) & 1) & (~((B >> 18) & 1)) & (Cout17)) | (((A >> 18) & 1) & ((B >> 18) & 1) & ~((Cout17))) | (((A >> 18) & 1) & ((B >> 18) & 1) & (Cout17))
    R19 = ((~((A >> 19) & 1)) & ((B >> 19) & 1) & ~((Cout18))) | (((A >> 19) & 1) & (~((B >> 19) & 1)) & ~((Cout18))) | ((~((A >> 19) & 1)) & (~((B >> 19) & 1)) & (Cout18)) | (((A >> 19) & 1) & ((B >> 19) & 1) & (Cout18))
    Cout19 = ((~((A >> 19) & 1)) & ((B >> 19) & 1) & (Cout18)) | (((A >> 19) & 1) & (~((B >> 19) & 1)) & (Cout18)) | (((A >> 19) & 1) & ((B >> 19) & 1) & ~((Cout18))) | (((A >> 19) & 1) & ((B >> 19) & 1) & (Cout18))
    R20 = ((~((A >> 20) & 1)) & ((B >> 20) & 1) & ~((Cout19))) | (((A >> 20) & 1) & (~((B >> 20) & 1)) & ~((Cout19))) | ((~((A >> 20) & 1)) & (~((B >> 20) & 1)) & (Cout19)) | (((A >> 20) & 1) & ((B >> 20) & 1) & (Cout19))
    Cout20 = ((~((A >> 20) & 1)) & ((B >> 20) & 1) & (Cout19)) | (((A >> 20) & 1) & (~((B >> 20) & 1)) & (Cout19)) | (((A >> 20) & 1) & ((B >> 20) & 1) & ~((Cout19))) | (((A >> 20) & 1) & ((B >> 20) & 1) & (Cout19))
    R21 = ((~((A >> 21) & 1)) & ((B >> 21) & 1) & ~((Cout20))) | (((A >> 21) & 1) & (~((B >> 21) & 1)) & ~((Cout20))) | ((~((A >> 21) & 1)) & (~((B >> 21) & 1)) & (Cout20)) | (((A >> 21) & 1) & ((B >> 21) & 1) & (Cout20))
    Cout21 = ((~((A >> 21) & 1)) & ((B >> 21) & 1) & (Cout20)) | (((A >> 21) & 1) & (~((B >> 21) & 1)) & (Cout20)) | (((A >> 21) & 1) & ((B >> 21) & 1) & ~((Cout20))) | (((A >> 21) & 1) & ((B >> 21) & 1) & (Cout20))
    R22 = ((~((A >> 22) & 1)) & ((B >> 22) & 1) & ~((Cout21))) | (((A >> 22) & 1) & (~((B >> 22) & 1)) & ~((Cout21))) | ((~((A >> 22) & 1)) & (~((B >> 22) & 1)) & (Cout21)) | (((A >> 22) & 1) & ((B >> 22) & 1) & (Cout21))
    Cout22 = ((~((A >> 22) & 1)) & ((B >> 22) & 1) & (Cout21)) | (((A >> 22) & 1) & (~((B >> 22) & 1)) & (Cout21)) | (((A >> 22) & 1) & ((B >> 22) & 1) & ~((Cout21))) | (((A >> 22) & 1) & ((B >> 22) & 1) & (Cout21))
    R23 = ((~((A >> 23) & 1)) & ((B >> 23) & 1) & ~((Cout22))) | (((A >> 23) & 1) & (~((B >> 23) & 1)) & ~((Cout22))) | ((~((A >> 23) & 1)) & (~((B >> 23) & 1)) & (Cout22)) | (((A >> 23) & 1) & ((B >> 23) & 1) & (Cout22))
    Cout23 = ((~((A >> 23) & 1)) & ((B >> 23) & 1) & (Cout22)) | (((A >> 23) & 1) & (~((B >> 23) & 1)) & (Cout22)) | (((A >> 23) & 1) & ((B >> 23) & 1) & ~((Cout22))) | (((A >> 23) & 1) & ((B >> 23) & 1) & (Cout22))
    R24 = ((~((A >> 24) & 1)) & ((B >> 24) & 1) & ~((Cout23))) | (((A >> 24) & 1) & (~((B >> 24) & 1)) & ~((Cout23))) | ((~((A >> 24) & 1)) & (~((B >> 24) & 1)) & (Cout23)) | (((A >> 24) & 1) & ((B >> 24) & 1) & (Cout23))
    Cout24 = ((~((A >> 24) & 1)) & ((B >> 24) & 1) & (Cout23)) | (((A >> 24) & 1) & (~((B >> 24) & 1)) & (Cout23)) | (((A >> 24) & 1) & ((B >> 24) & 1) & ~((Cout23))) | (((A >> 24) & 1) & ((B >> 24) & 1) & (Cout23))
    R25 = ((~((A >> 25) & 1)) & ((B >> 25) & 1) & ~((Cout24))) | (((A >> 25) & 1) & (~((B >> 25) & 1)) & ~((Cout24))) | ((~((A >> 25) & 1)) & (~((B >> 25) & 1)) & (Cout24)) | (((A >> 25) & 1) & ((B >> 25) & 1) & (Cout24))
    Cout25 = ((~((A >> 25) & 1)) & ((B >> 25) & 1) & (Cout24)) | (((A >> 25) & 1) & (~((B >> 25) & 1)) & (Cout24)) | (((A >> 25) & 1) & ((B >> 25) & 1) & ~((Cout24))) | (((A >> 25) & 1) & ((B >> 25) & 1) & (Cout24))
    R26 = ((~((A >> 26) & 1)) & ((B >> 26) & 1) & ~((Cout25))) | (((A >> 26) & 1) & (~((B >> 26) & 1)) & ~((Cout25))) | ((~((A >> 26) & 1)) & (~((B >> 26) & 1)) & (Cout25)) | (((A >> 26) & 1) & ((B >> 26) & 1) & (Cout25))
    Cout26 = ((~((A >> 26) & 1)) & ((B >> 26) & 1) & (Cout25)) | (((A >> 26) & 1) & (~((B >> 26) & 1)) & (Cout25)) | (((A >> 26) & 1) & ((B >> 26) & 1) & ~((Cout25))) | (((A >> 26) & 1) & ((B >> 26) & 1) & (Cout25))
    R27 = ((~((A >> 27) & 1)) & ((B >> 27) & 1) & ~((Cout26))) | (((A >> 27) & 1) & (~((B >> 27) & 1)) & ~((Cout26))) | ((~((A >> 27) & 1)) & (~((B >> 27) & 1)) & (Cout26)) | (((A >> 27) & 1) & ((B >> 27) & 1) & (Cout26))
    Cout27 = ((~((A >> 27) & 1)) & ((B >> 27) & 1) & (Cout26)) | (((A >> 27) & 1) & (~((B >> 27) & 1)) & (Cout26)) | (((A >> 27) & 1) & ((B >> 27) & 1) & ~((Cout26))) | (((A >> 27) & 1) & ((B >> 27) & 1) & (Cout26))
    R28 = ((~((A >> 28) & 1)) & ((B >> 28) & 1) & ~((Cout27))) | (((A >> 28) & 1) & (~((B >> 28) & 1)) & ~((Cout27))) | ((~((A >> 28) & 1)) & (~((B >> 28) & 1)) & (Cout27)) | (((A >> 28) & 1) & ((B >> 28) & 1) & (Cout27))
    Cout28 = ((~((A >> 28) & 1)) & ((B >> 28) & 1) & (Cout27)) | (((A >> 28) & 1) & (~((B >> 28) & 1)) & (Cout27)) | (((A >> 28) & 1) & ((B >> 28) & 1) & ~((Cout27))) | (((A >> 28) & 1) & ((B >> 28) & 1) & (Cout27))
    R29 = ((~((A >> 29) & 1)) & ((B >> 29) & 1) & ~((Cout28))) | (((A >> 29) & 1) & (~((B >> 29) & 1)) & ~((Cout28))) | ((~((A >> 29) & 1)) & (~((B >> 29) & 1)) & (Cout28)) | (((A >> 29) & 1) & ((B >> 29) & 1) & (Cout28))
    Cout29 = ((~((A >> 29) & 1)) & ((B >> 29) & 1) & (Cout28)) | (((A >> 29) & 1) & (~((B >> 29) & 1)) & (Cout28)) | (((A >> 29) & 1) & ((B >> 29) & 1) & ~((Cout28))) | (((A >> 29) & 1) & ((B >> 29) & 1) & (Cout28))
    R30 = ((~((A >> 30) & 1)) & ((B >> 30) & 1) & ~((Cout29))) | (((A >> 30) & 1) & (~((B >> 30) & 1)) & ~((Cout29))) | ((~((A >> 30) & 1)) & (~((B >> 30) & 1)) & (Cout29)) | (((A >> 30) & 1) & ((B >> 30) & 1) & (Cout29))
    Cout30 = ((~((A >> 30) & 1)) & ((B >> 30) & 1) & (Cout29)) | (((A >> 30) & 1) & (~((B >> 30) & 1)) & (Cout29)) | (((A >> 30) & 1) & ((B >> 30) & 1) & ~((Cout29))) | (((A >> 30) & 1) & ((B >> 30) & 1) & (Cout29))
    R31 = ((~((A >> 31) & 1)) & ((B >> 31) & 1) & ~((Cout30))) | (((A >> 31) & 1) & (~((B >> 31) & 1)) & ~((Cout30))) | ((~((A >> 31) & 1)) & (~((B >> 31) & 1)) & (Cout30)) | (((A >> 31) & 1) & ((B >> 31) & 1) & (Cout30))
    Cout31 = ((~((A >> 31) & 1)) & ((B >> 31) & 1) & (Cout30)) | (((A >> 31) & 1) & (~((B >> 31) & 1)) & (Cout30)) | (((A >> 31) & 1) & ((B >> 31) & 1) & ~((Cout30))) | (((A >> 31) & 1) & ((B >> 31) & 1) & (Cout30))
    R = (R0 << 0)+(R1 << 1)+(R2 << 2)+(R3 << 3)+(R4 << 4)+(R5 << 5)+(R6 << 6)+(R7 << 7)+(R8 << 8)+(R9 << 9)+(R10 << 10)+(R11 << 11)+(R12 << 12)+(R13 << 13)+(R14 << 14)+(R15 << 15)+(R16 << 16)+(R17 << 17)+(R18 << 18)+(R19 << 19)+(R20 << 20)+(R21 << 21)+(R22 << 22)+(R23 << 23)+(R24 << 24)+(R25 << 25)+(R26 << 26)+(R27 << 27)+(R28 << 28)+(R29 << 29)+(R30 << 30)+(R31 << 31)
    return R

def generate_32bits_adder():
    for i in range(32):
        A = '((A >> %d) & 1)' % i
        NotA = '(~%s)' % A
        B = '((B >> %d) & 1)' % i
        NotB = '(~%s)' % B
        Cin = '(Cout%d)' % (i - 1)
        NotCin = '~(%s)' % Cin

        if i == 0:
            Cin = '(0)'
            NotCin = '(1)'

        print 'R%d = (%s & %s & %s) | (%s & %s & %s) | (%s & %s & %s) | (%s & %s & %s)' % (
            i,
            NotA, B, NotCin,
            A, NotB, NotCin,
            NotA, NotB, Cin,
            A, B, Cin
        )
        print 'Cout%d = (%s & %s & %s) | (%s & %s & %s) | (%s & %s & %s) | (%s & %s & %s)' % (
            i,
            NotA, B, Cin,
            A, NotB, Cin,
            A, B, NotCin,
            A, B, Cin
        )

    print 'R = ' + '+'.join('(R%d << %d)' % (i, i) for i in range(32))

def main(argc, argv):
    print full_adder32(1337,1338)
    print full_adder32(0xfffffff0, 0xf + 1)
    return 1

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))

