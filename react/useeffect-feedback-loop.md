# useEffect feedback loop during user input

When a component has a local buffer (e.g., a string of digits the user is typing) and a derived value (e.g., a numeric representation) synced via `useEffect`, a feedback loop can corrupt the buffer mid-typing.

## The problem

Consider a duration input where the user types digits and the component converts them to a normalized value:

```javascript
const [digits, setDigits] = useState('000000'); // HH:MM:SS buffer
const [value, setValue] = useState(0);           // total seconds

function handleKeyDown(key) {
  const newDigits = digits.slice(1) + key;
  setDigits(newDigits);
  setValue(digitsToSeconds(newDigits));
}

// Sync external value changes back to digits
useEffect(() => {
  setDigits(secondsToDigits(value));
}, [value]);
```

When the user types `0`, `8`, `2`, `6` expecting `08:26`:

1. After typing `0`, `8` — digits are `'000008'` → 8 seconds → normalizes back to `'000008'` ✓
2. After typing `2` — digits are `'000082'` → 82 seconds
3. `useEffect` fires → `secondsToDigits(82)` = `'000122'` (1 min 22 sec)
4. `setDigits('000122')` **overwrites the buffer mid-typing**
5. Next keystroke `6` appends to the corrupted buffer → wrong result

The raw seconds value `82` is mathematically correct but gets normalized to `1:22` before the user finishes typing, destroying their input.

## The fix

Use a ref to skip the `useEffect` sync when the change originated from user input:

```javascript
const isTypingRef = useRef(false);

function handleKeyDown(key) {
  const newDigits = digits.slice(1) + key;
  setDigits(newDigits);
  isTypingRef.current = true;
  setValue(digitsToSeconds(newDigits));
}

useEffect(() => {
  if (isTypingRef.current) {
    isTypingRef.current = false;
    return; // skip — digits are already correct from handleKeyDown
  }
  setDigits(secondsToDigits(value));
}, [value]);
```

External updates (form reset, loading saved data) still sync correctly because they don't set the flag.

## Takeaway

Any time a `useEffect` writes back to the same state that triggered it — especially for formatted/normalized values — there's a risk of a feedback loop. If user input and external updates both change the same value, use a ref flag to distinguish the source and skip the redundant sync during typing.
