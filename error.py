import time

def steal_pie():
    from random import randint

    # Possible outcomes stored in a dictionary
    outcomes = {
        0: "pie successfully stolen",
        1: "fell off the counter",
        2: "owner walked in",
        3: "pie was too hot"
    }

    try:
        # Whiskers attempts to steal the pie
        outcome = randint(0, 3)  # Randomly determine the outcome
        if outcome == 1:
            raise Exception("Whiskers fell off the counter!")
        elif outcome == 2:
            raise Exception("The owner walked in!")
        elif outcome == 3:
            raise Exception("The pie was too hot!")
        else:
            print("Whiskers whispers: Yum, yum, yum!")

    except Exception as e:
        # Handle problems that might occur
        print(f"Whiskers growls: {str(e)}")

    else:
        # If no exceptions were raised
        print("Whiskers purrs: I'm going to enjoy this pie.")

    finally:
        # This block will execute no matter what
        print("Whiskers thinks: Time to plan my next adventure!")

# # Call the function to simulate the pie stealing
# for _ in range(10):
#     time.sleep(1)
#     steal_pie()

def test_cat_tower(sturdiness, height):
    try:
        # Check if the tower is tall enough for Whiskers' liking
        if height < 5:
            raise ValueError("This tower is too short for Whiskers!")

        # Assert that the tower is sturdy enough
        assert sturdiness >= 8, "This tower isn’t sturdy enough!"

        # If all is well
        print("Whiskers meows: This tower is just perfect!")

    except AssertionError as e:
        # Handle failed assertion
        print(f"Whiskers hisses: {str(e)}")

    except ValueError as e:
        # Handle other exceptions
        print(f"Whiskers sighs: {str(e)}")

    finally:
        # This will execute no matter what
        print("Whiskers thinks: Maybe I should just nap instead.")

# Example of calling the function
test_cat_tower(sturdiness=9, height=5)  # Should print that the tower is perfect
test_cat_tower(sturdiness=7, height=5)  # Should warn about sturdiness
test_cat_tower(sturdiness=10, height=4)  # Should warn about the height
