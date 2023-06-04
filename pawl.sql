CREATE TABLE `t_transaksi`(
    `id_kasir` BIGINT NOT NULL,
    `id_transaksi` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `tanggal` DATE NOT NULL,
    `total_harga` BIGINT NOT NULL,
    `jenis_transaksi` ENUM('') NOT NULL,
    `id_inventaris` BIGINT NOT NULL
);
CREATE TABLE `t_kasir`(
    `id_kasir` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `no_telpon` BIGINT NOT NULL
);
CREATE TABLE `t_inventaris`(
    `id_inventaris` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama` VARCHAR(255) NOT NULL,
    `stok` BIGINT NOT NULL,
    `harga_satuan` BIGINT NOT NULL,
    `tanggal` DATE NOT NULL,
    `total` BIGINT NOT NULL,
    `id_kasir` BIGINT NOT NULL,
    `id_pemasok` BIGINT NOT NULL,
    `id_kategori` BIGINT NOT NULL
);
CREATE TABLE `t_pemasok`(
    `id_kasir` BIGINT NOT NULL,
    `id_pemasok` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama_pemasok` VARCHAR(255) NOT NULL,
    `alamat` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `no_telpon` BIGINT NOT NULL
);
CREATE TABLE `t_kategori`(
    `id_kategori` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama_kategori` VARCHAR(255) NOT NULL
);
CREATE TABLE `t_detail`(
    `id_detail` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_user` BIGINT NOT NULL,
    `id_transaksi` BIGINT NOT NULL,
    `jumlah` BIGINT NOT NULL,
    `harga` BIGINT NOT NULL
);
CREATE TABLE `t_laporan`(
    `id_laporan` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nama` VARCHAR(255) NOT NULL,
    `jumlah` BIGINT NOT NULL,
    `harga_satuan` BIGINT NOT NULL,
    `total` BIGINT NOT NULL,
    `id_transaksi` BIGINT NOT NULL,
    `status` ENUM('') NOT NULL
);
ALTER TABLE
    `t_transaksi` ADD CONSTRAINT `t_transaksi_id_kasir_foreign` FOREIGN KEY(`id_kasir`) REFERENCES `t_kasir`(`id_kasir`);
ALTER TABLE
    `t_inventaris` ADD CONSTRAINT `t_inventaris_id_pemasok_foreign` FOREIGN KEY(`id_pemasok`) REFERENCES `t_pemasok`(`id_pemasok`);
ALTER TABLE
    `t_inventaris` ADD CONSTRAINT `t_inventaris_id_kategori_foreign` FOREIGN KEY(`id_kategori`) REFERENCES `t_kategori`(`id_kategori`);
ALTER TABLE
    `t_inventaris` ADD CONSTRAINT `t_inventaris_id_kasir_foreign` FOREIGN KEY(`id_kasir`) REFERENCES `t_kasir`(`id_kasir`);
ALTER TABLE
    `t_transaksi` ADD CONSTRAINT `t_transaksi_id_inventaris_foreign` FOREIGN KEY(`id_inventaris`) REFERENCES `t_inventaris`(`id_inventaris`);
ALTER TABLE
    `t_detail` ADD CONSTRAINT `t_detail_id_user_foreign` FOREIGN KEY(`id_user`) REFERENCES `t_kasir`(`id_kasir`);
ALTER TABLE
    `t_pemasok` ADD CONSTRAINT `t_pemasok_id_kasir_foreign` FOREIGN KEY(`id_kasir`) REFERENCES `t_kasir`(`id_kasir`);
ALTER TABLE
    `t_detail` ADD CONSTRAINT `t_detail_id_transaksi_foreign` FOREIGN KEY(`id_transaksi`) REFERENCES `t_transaksi`(`id_transaksi`);
ALTER TABLE
    `t_laporan` ADD CONSTRAINT `t_laporan_id_transaksi_foreign` FOREIGN KEY(`id_transaksi`) REFERENCES `t_transaksi`(`id_transaksi`);