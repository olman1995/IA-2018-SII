;Esta el template de las esclas
(deftemplate MAIN::scale
    (slot name (type STRING) (default ?DERIVE))
    (slot Mm (type INTEGER) (default ?DERIVE))
    (slot bemol (type INTEGER) (default ?DERIVE))
    (slot sostenido (type INTEGER) (default ?DERIVE))
)
;Cargade las escalas 
(deffacts MAIN::scale "scales"
    (scale (name "Do") (Mm 1) (bemol 0) (sostenido 0)) 
    (scale (name "Sol") (Mm 1) (bemol 0) (sostenido 1))
    (scale (name "Re") (Mm 1) (bemol 0) (sostenido 2))
    (scale (name "La") (Mm 1) (bemol 0) (sostenido 3))
    (scale (name "Mi") (Mm 1) (bemol 0) (sostenido 4))
    (scale (name "Si") (Mm 1) (bemol 0) (sostenido 5))
    (scale (name "Fa #") (Mm 1) (bemol 6) (sostenido 6))
    (scale (name "Sol b") (Mm 1) (bemol 6) (sostenido 6))
    (scale (name "Re b") (Mm 1) (bemol 5) (sostenido 0))
    (scale (name "La b") (Mm 1) (bemol 4) (sostenido 0))
    (scale (name "Mi b") (Mm 1) (bemol 3) (sostenido 0))
    (scale (name "Si b") (Mm 1) (bemol 2) (sostenido 0))
    (scale (name "Fa") (Mm 1) (bemol 1) (sostenido 0))
    (scale (name "la") (Mm 0) (bemol 0) (sostenido 0))
    (scale (name "mi") (Mm 0) (bemol 0) (sostenido 1))
    (scale (name "si") (Mm 0) (bemol 0) (sostenido 2))
    (scale (name "fa #") (Mm 0) (bemol 0) (sostenido 3))
    (scale (name "do #") (Mm 0) (bemol 0) (sostenido 4))
    (scale (name "sol b") (Mm 0) (bemol 0) (sostenido 5))
    (scale (name "mi b") (Mm 0) (bemol 6) (sostenido 6))
    (scale (name "re #") (Mm 0) (bemol 6) (sostenido 6))
    (scale (name "si b") (Mm 0) (bemol 5) (sostenido 0))
    (scale (name "fa") (Mm 0) (bemol 4) (sostenido 0))
    (scale (name "do") (Mm 0) (bemol 3) (sostenido 0))
    (scale (name "sol") (Mm 0) (bemol 2) (sostenido 0))
    (scale (name "re") (Mm 0) (bemol 1) (sostenido 0))
)
(deffunction get_scale (?scale ?Mm ?sb ?x)
    (do-for-all-facts ((?f ?scale)) 
        (if (= ?f:Mm ?Mm)
            then
                (if (= ?sb 1)
                    then
                        (if (= ?x ?f:sostenido)
                            then
                                (printout t ?f:name crlf)
                        )
                        
                    else
                        (if (= ?x ?f:bemol)
                            then
                                (printout t ?f:name crlf)
                        )
                )
        ) 
    )
)
(defrule MAIN::paso_1
    (p1 ?x) => 
    (if (> ?x 11) 
        then
            (printout t "Menores" crlf)
            (assert(p2 (- ?x 12)))
            (assert(Mm 0))
        else
            (printout t "Mayores" crlf)
            (assert(p2 ?x))
            (assert(Mm 1)) 
    )
)
(defrule paso_2
    (p2 ?x) => 
    (if (> ?x 6) 
        then
            (printout t "12-7" crlf)
            (assert(p3 (- 12 ?x)))
            (assert(sb 0))
        else
            (if (> ?x 4)
                then
                    (printout t "7-3" crlf)
                    (assert(p3 ?x))
                    (assert(sb 1))
                else
                    (printout t "4-0" crlf)
                    (assert(p3 ?x))
                    (assert(sb 1))
            ) 
    )
)
(defrule paso_3
    (p3 ?x)(sb ?sb)(Mm ?Mm) =>
    (get_scale scale ?Mm ?sb ?x)
)

