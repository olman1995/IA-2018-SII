;Esta el template de las esclas
(deftemplate MAIN::scale
    (slot name (type STRING) (default ?DERIVE))
    (slot Mm (type INTEGER) (default ?DERIVE))
    (slot bemol (type INTEGER) (default ?DERIVE))
    (slot sostenido (type INTEGER) (default ?DERIVE))
)
;Cargade las escalas 
(deffacts MAIN::scale "scales"
    (scale (name "C") (Mm 1) (bemol 0) (sostenido 0)) 
    (scale (name "G") (Mm 1) (bemol 0) (sostenido 1))
    (scale (name "D") (Mm 1) (bemol 0) (sostenido 2))
    (scale (name "A") (Mm 1) (bemol 0) (sostenido 3))
    (scale (name "E") (Mm 1) (bemol 0) (sostenido 4))
    (scale (name "B") (Mm 1) (bemol 0) (sostenido 5))
    (scale (name "F#/ Gb") (Mm 1) (bemol 6) (sostenido 6))
    (scale (name "Db") (Mm 1) (bemol 5) (sostenido 0))
    (scale (name "Ab") (Mm 1) (bemol 4) (sostenido 0))
    (scale (name "Eb") (Mm 1) (bemol 3) (sostenido 0))
    (scale (name "Bb") (Mm 1) (bemol 2) (sostenido 0))
    (scale (name "F") (Mm 1) (bemol 1) (sostenido 0))
    (scale (name "a") (Mm 0) (bemol 0) (sostenido 0))
    (scale (name "e") (Mm 0) (bemol 0) (sostenido 1))
    (scale (name "b") (Mm 0) (bemol 0) (sostenido 2))
    (scale (name "f#") (Mm 0) (bemol 0) (sostenido 3))
    (scale (name "c#") (Mm 0) (bemol 0) (sostenido 4))
    (scale (name "g#") (Mm 0) (bemol 0) (sostenido 5))
    (scale (name "eb/d#") (Mm 0) (bemol 6) (sostenido 6))
    (scale (name "bb") (Mm 0) (bemol 5) (sostenido 0))
    (scale (name "f") (Mm 0) (bemol 4) (sostenido 0))
    (scale (name "c") (Mm 0) (bemol 3) (sostenido 0))
    (scale (name "g") (Mm 0) (bemol 2) (sostenido 0))
    (scale (name "d") (Mm 0) (bemol 1) (sostenido 0))
)

(deffacts MAIN::start "starts"
	(r true)
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
								(halt)
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

(defrule MAIN::paso_0
    (r ?x) => 
    (printout t "Enter the number drawn (0-24): ")
	(assert (p1 (string-to-field (readline))))
)

(defrule paso_1
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
                    (printout t "7-5" crlf)
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

