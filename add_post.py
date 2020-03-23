# Simple script to add post usign GraphAPI.Uses test page
import facebook

page_id = "111466993816622"
page_token = "EAAC9ZBqHFFUYBADhAmnU6uJIZCTcNvMWhJr7jGe8FDTJ5VbuDmj7AkDP1Vorc7qnEWQ7OmOywSU87XHNzDlrKZCdTq3A4KRdrNdZBIu0FIuD9qC3ooX2pA2KOsmFfuSDFJtLYVmMyZCPdhETRwahUM3zkSlvEUJgVJLRxcPWUFozYLgawQFvA"
post_text = "test post2"

fb = facebook.GraphAPI(page_token)
fb.put_object(page_id, "feed", message=post_text)