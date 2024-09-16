

class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static int getMonth(int monthNumber) {
        switch (monthNumber) {
            case 1: return Calendar.JANUARY;
            case 2: return Calendar.FEBRUARY;
            case 3: return Calendar.MARCH;
            case 4: return Calendar.APRIL;
            case 5: return Calendar.MAY;
            case 6: return Calendar.JUNE;
            case 7: return Calendar.JULY;
            case 8: return Calendar.AUGUST;
            case 9: return Calendar.SEPTEMBER;
            case 10: return Calendar.OCTOBER;
            case 11: return Calendar.NOVEMBER;
            case 12: return Calendar.DECEMBER;
            default: 
                throw new IllegalArgumentException("Invalid: " + monthNumber);
        }
    }
    public static String findDay(int month, int day, int year) {

        int calMonth = getMonth(month);
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, calMonth, day);
        String numDay = calendar.getDisplayName(calendar.DAY_OF_WEEK, calendar.LONG, Locale.ENGLISH);
        numDay = numDay.toUpperCase();
        return numDay;

    }

}

