(define (problem puzzle)
  (:domain puzzle)
  (:objects
    t1 t2 t3 t4 t5 t6 t7 t8 p1 p2 p3 p4 p5 p6 p7 p8 p9
  )

  (:init
    (at t1 p1)
    (at t2 p5)
    (at t3 p7)
    (at t4 p6)
    (at t5 p8)
    (at t6 p3)
    (at t7 p2)
    (at t8 p4)
    (empty p9)

    (adjacent p1 p2)
    (adjacent p2 p1)
    
    (adjacent p1 p4) 
    (adjacent p4 p1)
    
    (adjacent p2 p5) 
    (adjacent p5 p2)
    
    (adjacent p2 p3) 
    (adjacent p3 p2)
    
    (adjacent p3 p6) 
    (adjacent p6 p3)
    
    (adjacent p4 p5)
    (adjacent p5 p4)
    
    (adjacent p4 p7)
    (adjacent p7 p4)
    
    (adjacent p5 p6)
    (adjacent p6 p5)
    
    (adjacent p5 p8)
    (adjacent p8 p5)
    
    (adjacent p6 p9)
    (adjacent p9 p6)
    
    (adjacent p7 p8)
    (adjacent p8 p7)
    
    (adjacent p8 p9) 
    (adjacent p9 p8)
  )

  (:goal (and
    (at t1 p1)
    (at t2 p2)
    (at t3 p3)
    (at t4 p4)
    (at t5 p5)
    (at t6 p6)
    (at t7 p7)
    (at t8 p8)
    (empty p9)
  ))
)
