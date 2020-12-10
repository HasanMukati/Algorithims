class Pair<X,Y>  { 
    private X key;
    private Y value;
    public Pair(X a1, Y a2) {
        key  = a1;
        value = a2;
    }
    public X getKey()  { return key; }
    public Y getValue() { return value; }
}
