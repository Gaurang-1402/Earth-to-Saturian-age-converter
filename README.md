

### Problem 5: How old are Earthlings?

Using the same assumptions about Earth units as in problem 4, can you write a program to determine your Saturnian age?
In this problem, you only need to determine Saturn-years. Here's the catch: Instead of entering the Earthling's age, you
enter their birthdate (the format is **[year][month][day]**):

```text
When was the Earthling you are talking to born on Earth? 19930315
This Earthling is 0.9204387024816433 Saturn-years old. How cute.
```

Do this in the function **`earth_to_saturnian_age_converter`**, inside the file
**[EarthToSaturnianAgeConverter.py](EarthToSaturnianAgeConverter.py)**.

**HINT**: You may not use any string methods in this problem, but modulo (`%`) and integer division (`//`) may come in
handy if you consider the birthdate (i.e. `19930315`) as an integer.
