/**
 * @author DREI
 */

import java.util.ArrayList;

public class DataRecords {
    private final ArrayList<Double> hoursStudy = new ArrayList<>();
    private String desc;

    // empty constructor
    public DataRecords(String desc) {
        this.desc = desc;
    }

    public void addRecord(int num) {
        double temp = num;  // No need for new Double(num)
        hoursStudy.add(temp);  // Add the value to the list (assuming hoursStudy is a List<Double>)
    }

    // for checking of inputs only
    public void displayDataRecords(){
        System.out.println(desc);
        for (int i = 0; i < hoursStudy.size(); i++) {
            System.out.println("record " + i + ": ");
        }
    }
}
