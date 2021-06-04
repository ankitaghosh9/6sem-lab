import fileinput

yearMcount = 0
yearFcount = 0
monMcount = 0
monFcount = 0

prevyear = '201001'

for line in fileinput.input():
    data = line.strip().split()
    if len(data) != 2:
        continue
    curryear, gender = data
    if prevyear[:4] == curryear[:4]:
        if prevyear[4:] == curryear[4:]:
            if gender == 'M':
                yearMcount += 1
                monMcount += 1
            else:
                yearFcount += 1
                monFcount += 1
        else:
            print(
                f"Month {prevyear[4:]}\t Male Births: {monMcount}, Female Births: {monFcount}, Total Births: {monFcount + monMcount}"
            )
            prevyear = curryear
            monMcount = monFcount = 0
            if gender == 'M':
                yearMcount += 1
                monMcount += 1
            else:
                yearFcount += 1
                monFcount += 1
    else:
        print(
            f"Year: {prevyear[:4]}\t Male Births: {yearMcount}\t Female Births:{yearFcount}\t Total Births: {yearFcount+yearMcount}\n\n"
        )
        yearMcount = 0
        yearFcount = 0
        prevyear = curryear
        if gender == 'M':
            yearMcount += 1
            monMcount += 1
        else:
            yearFcount += 1
            monFcount += 1

print(
    f"Year: {prevyear[:4]}\t Male Births: {yearMcount}\t Female Births:{yearFcount}\t Total Births: {yearFcount+yearMcount}\n\n"
)
