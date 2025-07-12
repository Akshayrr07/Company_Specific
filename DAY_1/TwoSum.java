package DAY_1;
    import java.util.*;

        public class TwoSum {
            private int[] array;
            private int target;
            private List<int[]> result;

            public TwoSum() {
                this.result = new ArrayList<>();
            }

            public void getInput(Scanner sc) {
                String[] arrStr = sc.nextLine().split(",");
                array = new int[arrStr.length];
                for (int i = 0; i < arrStr.length; i++) {
                    array[i] = Integer.parseInt(arrStr[i].trim());
                }
                target = Integer.parseInt(sc.nextLine().trim());
            }

            public List<int[]> twoSum() {
                result.clear();
                int n = array.length;
                for (int i = 0; i < n; i++) {
                    for (int j = i + 1; j < n; j++) {
                        if (array[i] + array[j] == target) {
                            result.add(new int[]{i, j});
                            break;
                        }
                    }
                }
                if (result.isEmpty()) {
                    return null;
                }
                return result;
            }

            public void display() {
                if (result != null && !result.isEmpty()) {
                    int[] pair = result.get(0);
                    System.out.println("(" + pair[0] + ", " + pair[1] + ")");
                } else {
                    System.out.println(-1);
                }
            }

            public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                TwoSum ts = new TwoSum();
                ts.getInput(sc);
                ts.twoSum();
                ts.display();
                sc.close();
            }
        }