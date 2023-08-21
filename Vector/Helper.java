class Vector {

    private double[] vector = new double[3];

    public Vector(double[] elements){
        this.vector = elements.clone();
    }

    @Override
    public String toString(){
        return "[" + this.vector[0] + "," +  this.vector[1] + "," +  this.vector[2] + "]";
    }

    public int size(){
        return this.vector.length;
    }

    public double get(int index){
        if (index <=2){
            return this.vector[index];
        }else{
            return -1;
        }
    }

    public double set(int index, double value){
        double previous = this.vector[index];
        this.vector[index] = value;

        return previous;
    }

    public Vector scalarProduct(double scalar){
        int n = this.size();

        double[] ans_dim = new double[n];

        for (int i=0;i<=n-1;i++){
            double dim = this.vector[i]*scalar;

            ans_dim[i] = dim;
        }

        Vector ans = new Vector(ans_dim);

        return ans;
    }

    public Vector add(Vector other){
        int n1 = this.size();
        int n2 = other.size();

        if (n1 != n2){
            return null;
        }

        double[] ans_dim = new double[n1];

        for (int i=0;i<=(n1-1);i++){
            ans_dim[i] = this.vector[i]+other.vector[i];
        }

        Vector ans = new Vector(ans_dim);

        return ans;
    }

    public boolean equals(Object other){
        
        if (other instanceof Vector){
            other = (Vector) other;
            int n1 = this.size();
            int n2 = other.size();

            if (n1 != n2){
                return false;
            }

            for (int i=0;i<=(n1-1);i++){
                if (this.vector[i] != other.vector[i]){
                    return false;
                }
            }

        }else{
            return false;
        }
    }
}

public class Helper{
    public static void main(String[] args){
        double[] elements = {1,2,3};
        double[] elements2 = {1,2,3,4};

        Vector a = new Vector(elements);
        Vector b = new Vector(elements2);

        System.out.print(a.equals(b));
    }
}