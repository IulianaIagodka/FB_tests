import facebook

#app_id = "208884153521478"
#app_secret = "4bb0ab67c979ad0d495260917821a8e5"
page_id = "111466993816622"
page_token = "EAAC9ZBqHFFUYBADhAmnU6uJIZCTcNvMWhJr7jGe8FDTJ5VbuDmj7AkDP1Vorc7qnEWQ7OmOywSU87XHNzDlrKZCdTq3A4KRdrNdZBIu0FIuD9qC3ooX2pA2KOsmFfuSDFJtLYVmMyZCPdhETRwahUM3zkSlvEUJgVJLRxcPWUFozYLgawQFvA"
#user_token = "EAAC9ZBqHFFUYBADhAmnU6uJIZCTcNvMWhJr7jGe8FDTJ5VbuDmj7AkDP1Vorc7qnEWQ7OmOywSU87XHNzDlrKZCdTq3A4KRdrNdZBIu0FIuD9qC3ooX2pA2KOsmFfuSDFJtLYVmMyZCPdhETRwahUM3zkSlvEUJgVJLRxcPWUFozYLgawQFvA"
fb = facebook.GraphAPI(page_token)
fb.put_object(page_id, "feed", message="test3")
