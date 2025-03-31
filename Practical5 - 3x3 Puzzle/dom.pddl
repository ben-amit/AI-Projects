(define (domain puzzle)
  (:requirements :strips)
  (:predicates
    (at ?t ?p)
    (empty ?p)
    (adjacent ?p1 ?p2)
  )

  (:action move
    :parameters
    (?t
    ?from
    ?to)
    :precondition
    (and
      (at ?t ?from)
      (empty ?to)
      (adjacent ?from ?to)
    )
    :effect
    (and
      (not (at ?t ?from))
      (at ?t ?to)
      (not (empty ?to))
      (empty ?from)
    )
  )
)
