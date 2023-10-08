(ns clojure-euler.prob1-10)

(defn sol1
  [lim]
  (apply +
    (filter #(or (zero? (mod % 3))
                 (zero? (mod % 5)))
            (range lim))))

(defn sol1a
  [lim]
  (->> (range lim)
      (filter #(or (zero? (mod % 3))
                   (zero? (mod % 5))))
      (reduce +)))

