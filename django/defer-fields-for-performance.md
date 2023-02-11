# Use `defer()` to limit fields fetched from models

This is a use-case I came across in a project that uses PostGIS and manages lat/long as a `PointField`. If you retrieve this GIS data, when you don't need it, it has an expensive overhead of fetching all metadata of GIS. This can cause a serious bottleneck in your APIs.

You can use `defer` method to limit the fields fetched.

For example:

```Python
restaurant_qs = Restaurant.objects.defer('point')
```

This will fetch all the restaurants without the `point` field -- which means avoid loading all GIS data that isn't needed.

A bit of warning though; if you end up accessing deferred field on any instance of queryset, it will make another trip to database to fetch that information.
