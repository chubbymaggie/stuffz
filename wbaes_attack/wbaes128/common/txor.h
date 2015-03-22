#pragma once

const unsigned char Txor[0x10][0x10] =
{
    {
        0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7,
        0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf
    },
    {
        0x1, 0x0, 0x3, 0x2, 0x5, 0x4, 0x7, 0x6,
        0x9, 0x8, 0xb, 0xa, 0xd, 0xc, 0xf, 0xe
    },
    {
        0x2, 0x3, 0x0, 0x1, 0x6, 0x7, 0x4, 0x5,
        0xa, 0xb, 0x8, 0x9, 0xe, 0xf, 0xc, 0xd
    },
    {
        0x3, 0x2, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4,
        0xb, 0xa, 0x9, 0x8, 0xf, 0xe, 0xd, 0xc
    },
    {
        0x4, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3,
        0xc, 0xd, 0xe, 0xf, 0x8, 0x9, 0xa, 0xb
    },
    {
        0x5, 0x4, 0x7, 0x6, 0x1, 0x0, 0x3, 0x2,
        0xd, 0xc, 0xf, 0xe, 0x9, 0x8, 0xb, 0xa
    },
    {
        0x6, 0x7, 0x4, 0x5, 0x2, 0x3, 0x0, 0x1,
        0xe, 0xf, 0xc, 0xd, 0xa, 0xb, 0x8, 0x9
    },
    {
        0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0,
        0xf, 0xe, 0xd, 0xc, 0xb, 0xa, 0x9, 0x8
    },
    {
        0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf,
        0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7
    },
    {
        0x9, 0x8, 0xb, 0xa, 0xd, 0xc, 0xf, 0xe,
        0x1, 0x0, 0x3, 0x2, 0x5, 0x4, 0x7, 0x6
    },
    {
        0xa, 0xb, 0x8, 0x9, 0xe, 0xf, 0xc, 0xd,
        0x2, 0x3, 0x0, 0x1, 0x6, 0x7, 0x4, 0x5
    },
    {
        0xb, 0xa, 0x9, 0x8, 0xf, 0xe, 0xd, 0xc,
        0x3, 0x2, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4
    },
    {
        0xc, 0xd, 0xe, 0xf, 0x8, 0x9, 0xa, 0xb,
        0x4, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3
    },
    {
        0xd, 0xc, 0xf, 0xe, 0x9, 0x8, 0xb, 0xa,
        0x5, 0x4, 0x7, 0x6, 0x1, 0x0, 0x3, 0x2
    },
    {
        0xe, 0xf, 0xc, 0xd, 0xa, 0xb, 0x8, 0x9,
        0x6, 0x7, 0x4, 0x5, 0x2, 0x3, 0x0, 0x1
    },
    {
        0xf, 0xe, 0xd, 0xc, 0xb, 0xa, 0x9, 0x8,
        0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0
    }
};
