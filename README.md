# Pushcrew - Web Push Notifications

[Pushcrew](https://pushcrew.com) is a service for sending push notifications from your web app.

# Getting started

Then set your authentication credentials:
```
>> import pushcrew
>> project = pushcrew.Api(auth_token='5374d7dfeffa2eb49965624ba7596a09')
```

* Get all segments.
```
import pushcrew
project = pushcrew.Api('5374d7dfeffa2eb49965624ba7596a09')
project.get_segments()
```

* Create segment.
```
import pushcrew
project = pushcrew.Api('5374d7dfeffa2eb49965624ba7596a09')
project.add_segment('Segment name')
```

* Add subscriber to segment.
```
import pushcrew
project = pushcrew.Api('5374d7dfeffa2eb49965624ba7596a09')
project.add_suscriber_to_segment('254256', ["8fcd1d68c82dd39d65ef8ea9a7948bbe"])
```

* Delete subscriber to segment.
```
import pushcrew
project = pushcrew.Api('5374d7dfeffa2eb49965624ba7596a09')
project.remove_subscriber_from_segment('254256', ["8fcd1d68c82dd39d65ef8ea9a7948bbe"])
```

* Get segment subscribers.
```
import pushcrew
project = pushcrew.Api('5374d7dfeffa2eb49965624ba7596a09')
project.get_subscribers_from_segment(segment_id=25)
```
