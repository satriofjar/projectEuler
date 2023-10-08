(ns clojure-euler.core)

(defn iter-prime
  [n i]
  (cond (= n i) true
        (zero? (rem n i)) false
        :else (iter-prime n (inc i))))
(defn prime?
  [x]
  (cond (<= x 1) false
        (= x 2) true
        (even? x) false
        :else (iter-prime x 3)))

(defn prime?2
  [x]
  (let [iter (fn iter [i]
               (cond (= x i) true
                     (zero? (rem x i)) false
                     :else (iter (inc i))))]
    (cond (<= x 1) false
          (= x 2) true
          :else (iter 2))))