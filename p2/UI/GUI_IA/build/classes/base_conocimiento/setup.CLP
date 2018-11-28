;Esta el template de las esclas
(deftemplate MAIN::scale
    (slot name (type STRING) (default ?DERIVE))
    (slot name_E (type STRING) (default ?DERIVE))
    (slot Mm (type INTEGER) (default ?DERIVE))
    (slot bemol (type INTEGER) (default ?DERIVE))
    (slot sostenido (type INTEGER) (default ?DERIVE))
)
;Cargade las escalas 
(deffacts MAIN::scale "scales"
    (scale (name "C") (name_E "Do") (Mm 1) (bemol 0) (sostenido 0)) 
    (scale (name "G") (name_E "Sol") (Mm 1) (bemol -1) (sostenido 1))
    (scale (name "D") (name_E "Re") (Mm 1) (bemol -1) (sostenido 2))
    (scale (name "A") (name_E "La") (Mm 1) (bemol -1) (sostenido 3))
    (scale (name "E") (name_E "Mi") (Mm 1) (bemol -1) (sostenido 4))

    (scale (name "B") (name_E "Si") (Mm 1) (bemol -1) (sostenido 5))
    (scale (name "C b") (name_E "Si") (Mm 1) (bemol 7) (sostenido -1))

    (scale (name "F #") (name_E "Fa #/Sol b ") (Mm 1) (bemol -1) (sostenido 6))
    (scale (name "G b") (name_E "Fa #/Sol b ") (Mm 1) (bemol 6) (sostenido -1))

    (scale (name "C #") (name_E "Re b") (Mm 1) (bemol -1) (sostenido 7))
    (scale (name "D b") (name_E "Re b") (Mm 1) (bemol 5) (sostenido -1))


    (scale (name "A b") (name_E "La B") (Mm 1) (bemol 4) (sostenido -1))
    (scale (name "E b") (name_E "Mi b") (Mm 1) (bemol 3) (sostenido -1))
    (scale (name "B b") (name_E "SI b") (Mm 1) (bemol 2) (sostenido -1))
    (scale (name "F") (name_E "Fa") (Mm 1) (bemol 1) (sostenido -1))
    (scale (name "a") (name_E "la") (Mm 0) (bemol 0) (sostenido 0))
    (scale (name "e") (name_E "mi") (Mm 0) (bemol -1) (sostenido 1))
    (scale (name "b") (name_E "si") (Mm 0) (bemol -1) (sostenido 2))
    (scale (name "f #") (name_E "fa #") (Mm 0) (bemol -1) (sostenido 3))
    (scale (name "c #") (name_E "do #") (Mm 0) (bemol -1) (sostenido 4))
    
    (scale (name "g #") (name_E "sol #") (Mm 0) (bemol 7) (sostenido -1))
    (scale (name "a b") (name_E "sol #") (Mm 0) (bemol -1) (sostenido 5))
    
    (scale (name "d #") (name_E "re # / mi b") (Mm 0) (bemol -1) (sostenido 6))
    (scale (name "e b") (name_E "re # / mi b") (Mm 0) (bemol 6) (sostenido -1))
    
    (scale (name "b b") (name_E "si b") (Mm 0) (bemol 5) (sostenido -1))
    (scale (name "a #") (name_E "si b") (Mm 0) (bemol -1) (sostenido 7))

    (scale (name "f") (name_E "fa") (Mm 0) (bemol 4) (sostenido -1))
    (scale (name "c") (name_E "do") (Mm 0) (bemol 3) (sostenido -1))
    (scale (name "g") (name_E "sol") (Mm 0) (bemol 2) (sostenido -1))
    (scale (name "d") (name_E "re") (Mm 0) (bemol 1) (sostenido -1))
)

(deffunction get_scale (?scale ?Mm ?sb ?x)
    (do-for-all-facts ((?f ?scale)) 
        (if (= ?f:Mm ?Mm)
            then
                (if (= ?sb 1)
                    then
                        (if (= ?x ?f:sostenido)
                            then
                                (assert(r ?f:name))					
                        )		
                            else
                                (if (= ?x ?f:bemol)
                                    then
                                        (assert(r ?f:name))
                                )
                )
        ) 
    )
)
(defrule  MAIN::paso_1
    (p1 ?x) => 
    (if (> ?x 12) 
        then
            (assert(p2 (- ?x 12)))
            (assert(Mm 0))
        else
            (assert(p2 ?x))
            (assert(Mm 1)) 
    )
)
(defrule paso_2
    (p2 ?x) => 
    (if (> ?x 7) 
        then
            (assert(p3 (- 12 ?x)))
            (assert(sb 0))
        else
            (if (> ?x 4)
                then
                    
                    (if (> (+ (mod (random) 6) 1) 3)
                        then
                            (assert(p3 ?x))
                            (assert(sb 0))
                        else
                            (assert(p3 ?x))
                            (assert(sb 1))
                    )
                else
                    (assert(p3 ?x))
                    (assert(sb 1))
            ) 
    )
)
(defrule paso_3
    (p3 ?x)(sb ?sb)(Mm ?Mm) =>
    (get_scale scale ?Mm ?sb ?x)
)

