# Not to use && for conditional rendering

Most tutorials on React will guide to use a pattern like this:

```javascript
condition && <ConditionalComponent>
```

If `condition` evaluates to `true`, `<ConditionalComponent>` will be rendered.
If `condition` evaluates to `false`, `<ConditionalComponent>` won't be rendered.

While this works for majority of scenarios (for conditions that evaluate to `boolean`), it isn't a good practice.

If a condition evaluates to:
- `0`, a `0` will be displayed in the UI prior to the rendered `ConditionalComponent`.
- `undefined`, an exception will happen and UI will break: `"Uncaught Error: Error(...): Nothing was returned from render. This usually means a return statement is missing. Or, to render nothing, return null."`


## Best practice

Javascript's ternary operator comes to rescue here. It would prevent the above issues from occuring

```javascript
condition ? <ConditionalComponent /> : null
```
