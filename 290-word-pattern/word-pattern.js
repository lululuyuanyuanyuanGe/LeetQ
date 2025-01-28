/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(/\s+/);
    if (words.length != pattern.length) {
        return false
    }

    const letter_map = new Map();
    const word_map = new Map()

    for (let i = 0; i<pattern.length; i++) {
        const w = words[i]
        const l = pattern[i]
        if (word_map.has(w)) {
            if (word_map.get(w) != l) {
                return false
            }}
        word_map.set(w, l)
        if (letter_map.has(l)) {
            if (letter_map.get(l) != w) {
                return false
            }
        }
        letter_map.set(l,w)
        
    }
    return true
};