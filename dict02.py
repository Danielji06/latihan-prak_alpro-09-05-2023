class SmartCard {
    private String nama;
    private long saldo;

    public void setNama(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public void setSaldo(long saldo) {
        if (saldo > 0) {
            this.saldo = saldo;
        }
    }

    public long getSaldo() {
        return saldo;
    }

    public void topUp(Voucher vch) {
        String kodeVoucher = vch.getKode();
        long nominal = vch.getNominal();

        if (kodeVoucher.equals("VC")) {
            System.out.println("Kode Voucher: " + kodeVoucher + " || Top up gagal! Kode voucher tidak valid.");
        } else if (kodeVoucher.equals("VC" + nominal)) {
            saldo += nominal;
            System.out.println("Kode Voucher: " + kodeVoucher + " || Top up sukses! Saldo " + nama + " saat ini Rp " + saldo);
        }
    }
}

class Voucher {
    private String kode;
    private long nominal;

    public void setNominal(long nominal) {
        this.nominal = nominal;
    }

    public long getNominal() {
        return nominal;
    }

    public String getKode() {
        if (nominal == 0) {
            kode = "VC";
        } else {
            kode = "VC" + nominal;
        }
        return kode;
    }
}

public class Main {
    public static void main(String[] args) {
        SmartCard card = new SmartCard();
        card.setNama("Guntur Putra");
        card.setSaldo(50000);

        Voucher voucher1 = new Voucher();
        voucher1.setNominal(0);

        Voucher voucher2 = new Voucher();
        voucher2.setNominal(50000);

        Voucher voucher3 = new Voucher();
        voucher3.setNominal(150000);

        System.out.println("Skenario 1: Top Up Gagal");
        card.topUp(voucher1);
        System.out.println("Saldo " + card.getNama() + " saat ini Rp " + card.getSaldo());

        System.out.println("\nSkenario 2: Top Up Sukses");
        card.topUp(voucher2);
        card.topUp(voucher3);
    }
}
