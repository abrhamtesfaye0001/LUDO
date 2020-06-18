import {Cell,Piece,Player} from "./classes.js";


a0 = new Cell("#a0", "open");
a1 = new Cell("#a1", "open");
a2 = new Cell("#a2", "open");
a3 = new Cell("#a3", "open");
a4 = new Cell("#a4", "open");
a5 = new Cell("#a5", "open");
a6 = new Cell("#a6", "open");
a7 = new Cell("#a7", "open");
a8 = new Cell("#a8", "open");
a9 = new Cell("#a9", "open");
a10 = new Cell("#a10", "open");
a11 = new Cell("#a11", "open");
a12 = new Cell("#a12", "open");
a13 = new Cell("#a13", "open");
a14 = new Cell("#a14", "open");
a15 = new Cell("#a15", "open");
a16 = new Cell("#a16", "open");
a17 = new Cell("#a17", "open");
a18 = new Cell("#a18", "open");
a19 = new Cell("#a19", "open");
a20 = new Cell("#a20", "open");
a21 = new Cell("#a21", "open");
a22 = new Cell("#a22", "open");
a23 = new Cell("#a23", "open");
a24 = new Cell("#a24", "open");
a25 = new Cell("#a25", "open");
a26 = new Cell("#a26", "open");
a27 = new Cell("#a27", "open");
a28 = new Cell("#a28", "open");
a29 = new Cell("#a29", "open");
a30 = new Cell("#a30", "open");
a31 = new Cell("#a31", "open");
a32 = new Cell("#a32", "open");
a33 = new Cell("#a33", "open");
a34 = new Cell("#a34", "open");
a35 = new Cell("#a35", "open");
a36 = new Cell("#a36", "open");
a37 = new Cell("#a37", "open");
a38 = new Cell("#a38", "open");
a39 = new Cell("#a39", "open");
a40 = new Cell("#a40", "open");
a41 = new Cell("#a41", "open");
a42 = new Cell("#a42", "open");
a43 = new Cell("#a43", "open");
a44 = new Cell("#a44", "open");
a45 = new Cell("#a45", "open");
a46 = new Cell("#a46", "open");
a47 = new Cell("#a47", "open");

r0 = new Cell("#r0", "start");
r1 = new Cell("#r1", "homeRun");
r2 = new Cell("#r2", "homeRun");
r3 = new Cell("#r3", "homeRun");
r4 = new Cell("#r4", "homeRun");
r5 = new Cell("#r5", "homeRun");
r6 = new Cell("#r6", "home");

r7 = new Cell("#r7", "station");
r8 = new Cell("#r8", "station");
r9 = new Cell("#r9", "station");
r10 = new Cell("#r10", "station");

g0 = new Cell("#g0", "start");
g1 = new Cell("#g1", "homeRun");
g2 = new Cell("#g2", "homeRun");
g3 = new Cell("#g3", "homeRun");
g4 = new Cell("#g4", "homeRun");
g5 = new Cell("#g5", "homeRun");
g6 = new Cell("#g6", "home");

g7 = new Cell("#g7", "station");

g8 = new Cell("#g8", "station");
g9 = new Cell("#g9", "station");
g10 = new Cell("#g10", "station");

b0 = new Cell("#b0", "start");
b1 = new Cell("#b1", "homeRun");
b2 = new Cell("#b2", "homeRun");
b3 = new Cell("#b3", "homeRun");
b4 = new Cell("#b4", "homeRun");
b5 = new Cell("#b5", "homeRun");
b6 = new Cell("#b6", "home");
b7 = new Cell("#b7", "station");
b8 = new Cell("#b8", "station");
b9 = new Cell("#b9", "station");
b10 = new Cell("#b10", "station");

y0 = new Cell("#y0", "start");
y1 = new Cell("#y1", "homeRun");
y2 = new Cell("#y2", "homeRun");
y3 = new Cell("#y3", "homeRun");
y4 = new Cell("#y4", "homeRun");
y5 = new Cell("#y5", "homeRun");
y6 = new Cell("#y6", "home");
y7 = new Cell("#y7", "station");
y8 = new Cell("#y8", "station");
y9 = new Cell("#y9", "station");
y10 = new Cell("#y10", "station");


redPath = [r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, r1, r2, r3, r4, r5, r6];
greenPath = [g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, g1, g2, g3, g4, g5, g6];
bluePath = [b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6];
yellowPath = [y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, y1, y2, y3, y4, y5, y6];





rp0 = new Piece("#rp0", r7, redPath);
rp1 = new Piece("#rp1", r8, redPath);
rp2 = new Piece("#rp2", r9, redPath);
rp3 = new Piece("#rp3", r10, redPath);





gp0 = new Piece("#gp0", g7, greenPath);
gp1 = new Piece("#gp1", g8, greenPath);
gp2 = new Piece("#gp2", g9, greenPath);
gp3 = new Piece("#gp3", g10, greenPath);



bp0 = new Piece("#bp0", b7, bluePath);
bp1 = new Piece("#bp1", b8, bluePath);
bp2 = new Piece("#bp2", b9, bluePath);
bp3 = new Piece("#bp3", b10, bluePath);


yp0 = new Piece("#yp0", y7, yellowPath);
yp1 = new Piece("#yp1", y8, yellowPath);
yp2 = new Piece("#yp2", y9, yellowPath);
yp3 = new Piece("#yp3", y10, yellowPath);


export {redPath,greenPath,yellowPath,bluePath};