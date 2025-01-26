/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if (s.length !== t.length) {
        return false
    }

    let sToT = new Map();
    let tToS = new Map();

    for (let i = 0; i < s.length; i++) {
        let charS = s[i]
        let charT = t[i]

        if (sToT.has(charS)) {
            if (sToT.get(charS) !== charT) {
                return false;
            }
        } else {
            sToT.set(charS, charT)
        }

        if (tToS.has(charT)) {
            if (tToS.get(charT) !== charS) {
                return false
            }
        } else {
            tToS.set(charT, charS)
        }
    }
    return true
};