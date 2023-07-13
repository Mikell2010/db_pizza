-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_pizza
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_pizza
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_pizza` DEFAULT CHARACTER SET utf8 ;
USE `db_pizza` ;

-- -----------------------------------------------------
-- Table `db_pizza`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pizza`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NOT NULL,
  `ciudad` VARCHAR(255) NOT NULL,
  `region` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME NOT NULL DEFAULT now(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_pizza`.`pizzas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pizza`.`pizzas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `size` VARCHAR(255) NOT NULL,
  `crust` VARCHAR(255) NOT NULL,
  `cantidad` INT NOT NULL,
  `descripcion_pizza` TEXT NOT NULL,
  `nombre_pizza` VARCHAR(255) NOT NULL,
  `precio` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME NOT NULL DEFAULT now(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nombre_pizza_UNIQUE` (`nombre_pizza` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_pizza`.`favoritos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pizza`.`favoritos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `pizza_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME NOT NULL DEFAULT now(),
  INDEX `fk_usuarios_has_pizzas_pizzas1_idx` (`pizza_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_pizzas_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_usuarios_has_pizzas_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_pizza`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_pizzas_pizzas1`
    FOREIGN KEY (`pizza_id`)
    REFERENCES `db_pizza`.`pizzas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_pizza`.` pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pizza`.` pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `pizza_id` INT NOT NULL,
  `fecha_pedido` DATETIME NOT NULL DEFAULT now(),
  `methods` VARCHAR(255) NOT NULL,
  `toppings_elegidos` VARCHAR(255) NOT NULL,
  `precio` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME NOT NULL DEFAULT now(),
  INDEX `fk_usuarios_has_ pedidos_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  INDEX `fk_ pedidos_pizzas1_idx` (`pizza_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_ pedidos_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_pizza`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ pedidos_pizzas1`
    FOREIGN KEY (`pizza_id`)
    REFERENCES `db_pizza`.`pizzas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_pizza`.`toppings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_pizza`.`toppings` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `precio` INT UNSIGNED NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT now(),
  `updated_at` DATETIME NOT NULL DEFAULT now(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
