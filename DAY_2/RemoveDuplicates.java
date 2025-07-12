package DAY_2;

import java.util.*;

public class RemoveDuplicates {
    
    private int[] a;

    public RemoveDuplicates() {
    }

    public void getInput(Scanner sc){
        String[] aStr = sc.nextLine().split(",");
        a = new int[aStr.length];
        for (int i =0; i < aStr.length; i++){
            a[i] = Integer.parseInt(aStr[i].trim());
        }
    }

    public List<Integer> findDuplicates() {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();
        for (int num : a) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }
        return new ArrayList<>(duplicates);
    }
}
