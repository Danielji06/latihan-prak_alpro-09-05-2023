public class Buku {
    private static int nextNum = 1;

    private String kode;
    private String judul;
    private String penulis;
    private long harga;
    private int stok;

    // Constructor
    public Buku(String argJudul, String argPenulis, long argHarga, int argStok) {
        judul = argJudul;
        penulis = argPenulis;
        if (argHarga <= 0) {
            harga = 0;
        } else {
            harga = argHarga;
        }
        if (argStok <= 0) {
            stok = 0;
        } else {
            stok = argStok;
        }
        generateKode();
    }

    // Method untuk generate kode buku
    private void generateKode() {
        kode = "NV" + String.format("%06d", nextNum);
        nextNum++;
    }

    // Getter methods
    public String getKode() {
        return kode;
    }

    public String getJudul() {
        return judul;
    }

    public String getPenulis() {
        return penulis;
    }

    public long getHarga() {
        return harga;
    }

    public int getStok() {
        return stok;
    }
}
