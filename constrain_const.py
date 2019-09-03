def constrain_const(n):

 # Func =[ Dimension(D) , parameter(p) , pop-size(Ng)]
    F1 = [ 1 , 1 ]
    F2 = [ 2 , 1 ]
    F3 = [ 2 , 2 ]
    F4 = [ 5 , 1 ]
    F5 = [ 5 , 3 ]
    F6 = [ 5 , 5 ]
    F7 = [ 10, 1 ]
    F8 = [ 10, 3 ]
    F9 = [ 10, 5 ]
    F10 =[  1, 1 ]
    F11 =[  2, 4 ]
    F12 =[  2, 8 ]
    F13 =[  1, 1 ]
    F14 =[  1, 1 ]
    F15 =[  2, 1 ]
    F16 =[  2, 1 ]
    F17 =[  3, 1 ]
    F18 =[  5, 1 ]

    benchmark_func=[F1,F2,F3,F4,F5,F6,F7,F8,F9,
                    F10,F11,F12,F13,F14,F15,F16,
                    F17,F18]

    return benchmark_func[n-1]
