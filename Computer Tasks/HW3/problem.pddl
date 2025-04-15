(define (problem puzzle)
  (:domain puzzle)
  (:objects
    t1 t2 t3  p1 p2 p3 p4 
  )

  (:init
    (at t2 p1)
    (at t1 p2)
    (at t3 p3)
    (empty p4)

    (adjacent p1 p2)
    (adjacent p2 p1)

    (adjacent p1 p3)
    (adjacent p3 p1)

    (adjacent p2 p4)
    (adjacent p4 p2)

    (adjacent p3 p4)
    (adjacent p4 p3)

  )

  (:goal (and
    (at t1 p1)
    (at t2 p2)
    (at t3 p3)
    (empty p4)
  ))
)